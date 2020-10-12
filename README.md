# ALPR [![license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/YuTingChow/ALPR/blob/master/LICENSE)

## An Automatic License Plate Recognition Algorithm using YOLOv5 and EasyOCR.

## Sample Output
![sample](sample/sample1.jpg)

The algorithm is divided into 2 stages, first locating license plates (bounding boxes) then readout the characters.

Output: readout characters, license plate confidence level 

# Introduction 
This project is aimed at US License Plate Recognition for parking management. 
The YOLOv5 framework is adopted from https://github.com/ultralytics/yolov5 and trained using images from OpenALPR benchmark dataset https://github.com/openalpr/benchmarks.

For EasyOCR https://github.com/JaidedAI/EasyOCR, default settings and weights are used.

# Requirements
Python 3.8 or later with all [requirements.txt](requirements.txt) dependencies installed, including `torch>=1.6`. To install run:
```bash
$ git clone https://github.com/YuTingChow/ALPR.git
$ cd ALPR
$ pip install -r ./requirements.txt
```

# Tests
To test if the environment is setup correctly, you may run

```bash
$ python ./src/detect.py
```
The expected output is as follows:
```bash
Namespace(agnostic_nms=False, augment=False, classes=None, conf_thres=0.5, device='', img_size=640, iou_thres=0.5, output='inference/output', save_txt=False, source='tests/images', update=False, view_img=False, weights='best.pt')
Using CUDA device0 _CudaDeviceProperties(name='Your GPU Name', total_memory=XXXXMB)

Fusing layers... 
Model Summary: 191 layers, 7.25509e+06 parameters, 0 gradients
image 1/3 ~/alpr-insight/ALPR/tests/images/car7.jpg: 0   I0DTM59
448x640 1 license_plates, Done. (0.069s)
image 2/3 ~/alpr-insight/ALPR/tests/images/car8.jpg: 0   FZRULZ
640x512 1 license_plates, Done. (0.042s)
image 3/3 ~/alpr-insight/ALPR/tests/images/car9-2.jpg: 0   4639520
384x640 1 license_plates, Done. (0.043s)
Results saved to inference/output
Done.
```

# Inference 

Inference can be run on images or videos. Results are saved to './inference/output'

```bash
$ python ./src/detect.py --source  file.jpg  # image 
                            file.mp4  # video
                            path/  # directory
                            path/*.jpg  # glob
```

To run inference on images in the './tests/images' folder:
```bash
$ python ./src/detect.py --source ./tests/images/
```
# Custom Training

You can train the network from scratch with your own data as follows:
```bash
$ python ./src/train.py --data ./data/licensePlate.yaml --cfg models/yolov5s.yaml --weights '' --batch-size 16
```
You just need to replace the data path to the training and validation set in `licensePlate.yaml`.

![results](sample/results.png)

For the requirements of data labelling, please refer to this [wiki](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data).