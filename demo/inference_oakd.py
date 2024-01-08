import torch
import matplotlib.pyplot as plt
from mmengine.model.utils import revert_sync_batchnorm
from mmseg.apis import init_model, inference_model, show_result_pyplot
import cv2
import argparse
import numpy as np 
from mmdeploy_runtime import Segmentor
import depthai as dai
import time

# config_file = '../configs/test/test.py'
# checkpoint_file = '../work_dirs/test/iter_40000.pth'

def parse_args():
    parser = argparse.ArgumentParser(
        description='show how to use sdk python api')
    parser.add_argument('--device_name', default='cuda' ,help='name of device, cuda or cpu')
    parser.add_argument('--config_file', default='/home/configs/test/test.py', 
                        help = 'path of config file')
    parser.add_argument('--checkpoint_file', default='/home/work_dirs/test/iter_40000.pth',
                        help='path of checkpoint file')
    args = parser.parse_args()
    return args


def get_palette(num_classes=256):
    state = np.random.get_state()
    # random color
    np.random.seed(42)
    palette = np.random.randint(0, 256, size=(num_classes, 3))
    np.random.set_state(state)
    return [tuple(c) for c in palette]

pipeline = dai.Pipeline()

camRgb = pipeline.createColorCamera()
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setInterleaved(False)
camRgb.setFps(40)

rgbout = pipeline.createXLinkOut()
rgbout.setStreamName("RGB")
camRgb.video.link(rgbout.input)

args = parse_args()

model = init_model(args.config_file, args.checkpoint_file, device=args.device_name)

with dai.Device(pipeline) as device:
    device.startPipeline()
    qRgb = device.getOutputQueue(name="RGB", maxSize=4, blocking=False)

    frame_count = 0
    start_time = time.time()

    while True:
        inRgb = qRgb.get()  # blocking call, will wait until a new data has arrived
        frame_count += 1

        # Calculate FPS
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time > 0:
            fps = frame_count / elapsed_time

        # Display FPS on frame
        frame = inRgb.getCvFrame()
        frame = cv2.resize(frame,(960,540))
        
        a = time.time()
        result = inference_model(model, frame)
        #print("time: ",time.time()- a)

        vis_result = result.pred_sem_seg.data.cpu().numpy().astype(np.uint8)
        vis_result = np.stack([np.squeeze(vis_result)]*3, axis=2)
        #print("vis_result.shpa : ",vis_result.shape)
        b= time.time()
        #vis_result = show_result_pyplot(model, frame, result, show=False)
        #print("time1 ",time.time()-b)
        print("vis_result.unique : ",np.unique(vis_result))

        if np.unique(vis_result).shape[0] > 1:
            vis_result *= int(255/(np.unique(vis_result).shape[0]-1))
        # cv2.putText(
        #     vis_result,
        #     f"FPS: {fps:.2f}",
        #     (10, 30),
        #     cv2.FONT_HERSHEY_SIMPLEX,
        #     1,
        #     (0, 255, 255),
        #     2,
        # )
        cv2.imshow("rgb", frame)
        cv2.imshow("mask", vis_result)

        if cv2.waitKey(1) == ord("q"):
            break
