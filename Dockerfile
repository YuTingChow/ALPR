# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM nvcr.io/nvidia/pytorch:20.09-py3

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6 -y
# Install dependencies
RUN pip install --upgrade pip
RUN git clone https://github.com/YuTingChow/ALPR.git

WORKDIR /workspace/ALPR
RUN pip install -r requirements.txt
RUN python src/detect.py

