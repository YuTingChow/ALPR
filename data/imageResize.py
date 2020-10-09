import argparse
import cv2
import os
import threading
class ResizeThread(threading.Thread):
    def __init__(self, threadID, name, inputFolder, outputFolder, filename, new_shape):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.inputFolder = inputFolder
        self.outputFolder = outputFolder
        self.filename = filename
        self.new_shape = new_shape
    def run(self):
        # print("Starting.. " + self.name)
        SingleThreadProcess(self.inputFolder, self.outputFolder, self.filename, self.new_shape)

def SingleThreadProcess(inputFolder, outputFolder, filename, new_shape):
    img = cv2.imread(os.path.join(inputFolder,filename))
    if img is not None:                
        aspectR =  img.shape[0] / img.shape[1]
        imgOut = cv2.resize(img, (new_shape, int(new_shape*aspectR)), interpolation=cv2.INTER_LINEAR)
        print(img.shape, filename,' to ', imgOut.shape, filename)
        cv2.imwrite(outputFolder + filename, imgOut)
    
    

def imageResize():
    inputFolder = opt.source
    outputFolder = opt.output
    new_shape = opt.img_size
    nthread = opt.nthread
    
    threads = []
    i=0
    fileList = sorted(os.listdir(inputFolder))
    for filename in fileList:
        if filename.endswith(".jpg"):
            thread = ResizeThread(i, "Thread-"+str(i), inputFolder, outputFolder, filename, new_shape)
            threads.append(thread)
            thread.start()
            i+=1
        if i==nthread:
            for t in threads:
                t.join()
            i=0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='/raw', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--output', type=str, default='/preprocessed', help='output folder')  # output folder
    parser.add_argument('--img-size', type=int, default='640', help='image resize')  # output folder
    parser.add_argument('--nthread', type=int, default='1', help='no. of processing threads') # no. of proessing threads
    opt = parser.parse_args()
    
    imageResize()
    