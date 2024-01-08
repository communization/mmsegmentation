_base_ = [
    '../_base_/models/deeplabv3plus_r50-d8.py', '../_base_/datasets/DLoop.py',
    '../_base_/default_runtime.py', '../_base_/schedules/schedule_40k.py'
]
crop_size = (540, 960) #(540, 960)
#train_pipeline = dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
data_preprocessor = dict(size=crop_size)

# model = dict(
#     # pretrained='open-mmlab://resnet101_v1c',
#     # backbone=dict(depth=101),
#     data_preprocessor=data_preprocessor,
#     decode_head=dict(num_classes=2),
#     auxiliary_head=dict(num_classes=2))
# train_dataloader = dict(dataset=dict(times=20000), batch_size=1)

model = dict(
    data_preprocessor=data_preprocessor,
    pretrained='open-mmlab://resnet101_v1c',
    backbone=dict(
        depth=101,
        dilations=(1, 1, 1, 2),
        strides=(1, 2, 2, 1),
        multi_grid=(1, 2, 4)),
    decode_head=dict(
        dilations=(1, 6, 12, 18),
        num_classes=2,    ),
    auxiliary_head=dict(num_classes=2),)
train_dataloader = dict(dataset=dict(times=40000), batch_size=2)