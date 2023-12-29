_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py', '../_base_/datasets/test_water.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
crop_size = (512, 512)#(512, 1024)
train_pipeline = dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),

data_preprocessor = dict(size=crop_size)
model = dict(
    data_preprocessor=data_preprocessor,
    decode_head=dict(num_classes=3),
    auxiliary_head=dict(num_classes=3))

train_dataloader = dict(batch_size=2)