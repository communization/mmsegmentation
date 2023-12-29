Collections = [
    dict(
        Frameworks=[
            'PyTorch',
        ],
        License='Apache License 2.0',
        Metadata=dict({'Training Data': [
            'Cityscapes',
        ]}),
        Name='BiSeNetV2',
        Paper=dict(
            Title=
            'Bisenet v2: Bilateral Network with Guided Aggregation for Real-time Semantic Segmentation',
            URL='https://arxiv.org/abs/2004.02147'),
        README='configs/bisenetv2/README.md'),
]
Models = [
    dict({
        'Code':
        'https://github.com/open-mmlab/mmsegmentation/blob/v0.18.0/mmseg/models/backbones/bisenetv2.py#L545',
        'Config':
        'configs/bisenetv2/bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024.py',
        'Framework':
        'PyTorch',
        'In Collection':
        'BiSeNetV2',
        'Metadata':
        dict({
            'Architecture': [
                'BiSeNetV2',
                'BiSeNetV2',
            ],
            'Batch Size': 16,
            'Memory (GB)': 7.64,
            'Training Data': 'Cityscapes',
            'Training Resources': '4x V100 GPUS'
        }),
        'Name':
        'bisenetv2_fcn_4xb4-160k_cityscapes-1024x1024',
        'Paper':
        dict(
            Title=
            'Bisenet v2: Bilateral Network with Guided Aggregation for Real-time Semantic Segmentation',
            URL='https://arxiv.org/abs/2004.02147'),
        'Results':
        dict(
            Dataset='Cityscapes',
            Metrics=dict({
                'mIoU': 73.21,
                'mIoU(ms+flip)': 75.74
            }),
            Task='Semantic Segmentation'),
        'Training log':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_4x4_1024x1024_160k_cityscapes/bisenetv2_fcn_4x4_1024x1024_160k_cityscapes_20210902_015551.log.json',
        'Weights':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_4x4_1024x1024_160k_cityscapes/bisenetv2_fcn_4x4_1024x1024_160k_cityscapes_20210902_015551-bcf10f09.pth'
    }),
    dict({
        'Code':
        'https://github.com/open-mmlab/mmsegmentation/blob/v0.18.0/mmseg/models/backbones/bisenetv2.py#L545',
        'Config':
        'configs/bisenetv2/bisenetv2_fcn_4xb4-ohem-160k_cityscapes-1024x1024.py',
        'Framework':
        'PyTorch',
        'In Collection':
        'BiSeNetV2',
        'Metadata':
        dict({
            'Architecture': [
                'BiSeNetV2',
                'BiSeNetV2',
            ],
            'Batch Size': 16,
            'Memory (GB)': 7.64,
            'Training Data': 'Cityscapes',
            'Training Resources': '4x V100 GPUS'
        }),
        'Name':
        'bisenetv2_fcn_4xb4-ohem-160k_cityscapes-1024x1024',
        'Paper':
        dict(
            Title=
            'Bisenet v2: Bilateral Network with Guided Aggregation for Real-time Semantic Segmentation',
            URL='https://arxiv.org/abs/2004.02147'),
        'Results':
        dict(
            Dataset='Cityscapes',
            Metrics=dict({
                'mIoU': 73.57,
                'mIoU(ms+flip)': 75.8
            }),
            Task='Semantic Segmentation'),
        'Training log':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_ohem_4x4_1024x1024_160k_cityscapes/bisenetv2_fcn_ohem_4x4_1024x1024_160k_cityscapes_20210902_112947.log.json',
        'Weights':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_ohem_4x4_1024x1024_160k_cityscapes/bisenetv2_fcn_ohem_4x4_1024x1024_160k_cityscapes_20210902_112947-5f8103b4.pth'
    }),
    dict({
        'Code':
        'https://github.com/open-mmlab/mmsegmentation/blob/v0.18.0/mmseg/models/backbones/bisenetv2.py#L545',
        'Config':
        'configs/bisenetv2/bisenetv2_fcn_4xb8-160k_cityscapes-1024x1024.py',
        'Framework':
        'PyTorch',
        'In Collection':
        'BiSeNetV2',
        'Metadata':
        dict({
            'Architecture': [
                'BiSeNetV2',
                'BiSeNetV2',
            ],
            'Batch Size': 32,
            'Memory (GB)': 15.05,
            'Training Data': 'Cityscapes',
            'Training Resources': '4x V100 GPUS'
        }),
        'Name':
        'bisenetv2_fcn_4xb8-160k_cityscapes-1024x1024',
        'Paper':
        dict(
            Title=
            'Bisenet v2: Bilateral Network with Guided Aggregation for Real-time Semantic Segmentation',
            URL='https://arxiv.org/abs/2004.02147'),
        'Results':
        dict(
            Dataset='Cityscapes',
            Metrics=dict({
                'mIoU': 75.76,
                'mIoU(ms+flip)': 77.79
            }),
            Task='Semantic Segmentation'),
        'Training log':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_4x8_1024x1024_160k_cityscapes/bisenetv2_fcn_4x8_1024x1024_160k_cityscapes_20210903_000032.log.json',
        'Weights':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_4x8_1024x1024_160k_cityscapes/bisenetv2_fcn_4x8_1024x1024_160k_cityscapes_20210903_000032-e1a2eed6.pth'
    }),
    dict({
        'Code':
        'https://github.com/open-mmlab/mmsegmentation/blob/v0.18.0/mmseg/models/backbones/bisenetv2.py#L545',
        'Config':
        'configs/bisenetv2/bisenetv2_fcn_4xb4-amp-160k_cityscapes-1024x1024.py',
        'Framework':
        'PyTorch',
        'In Collection':
        'BiSeNetV2',
        'Metadata':
        dict({
            'Architecture': [
                'BiSeNetV2',
                'BiSeNetV2',
            ],
            'Batch Size': 16,
            'Memory (GB)': 5.77,
            'Training Data': 'Cityscapes',
            'Training Resources': '4x V100 GPUS'
        }),
        'Name':
        'bisenetv2_fcn_4xb4-amp-160k_cityscapes-1024x1024',
        'Paper':
        dict(
            Title=
            'Bisenet v2: Bilateral Network with Guided Aggregation for Real-time Semantic Segmentation',
            URL='https://arxiv.org/abs/2004.02147'),
        'Results':
        dict(
            Dataset='Cityscapes',
            Metrics=dict({
                'mIoU': 73.07,
                'mIoU(ms+flip)': 75.13
            }),
            Task='Semantic Segmentation'),
        'Training log':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_fp16_4x4_1024x1024_160k_cityscapes/bisenetv2_fcn_fp16_4x4_1024x1024_160k_cityscapes_20210902_045942.log.json',
        'Weights':
        'https://download.openmmlab.com/mmsegmentation/v0.5/bisenetv2/bisenetv2_fcn_fp16_4x4_1024x1024_160k_cityscapes/bisenetv2_fcn_fp16_4x4_1024x1024_160k_cityscapes_20210902_045942-b979777b.pth'
    }),
]
