import argparse
import cv2
import os

def dataPreprocessing():
    os.environ['DISPLAY'] = ':1'
    inputFolder = opt.source
    outputFolder = opt.output
    for filename in os.listdir(inputFolder):
        if filename.endswith(".jpg"):
            img = cv2.imread(os.path.join(inputFolder,filename))
            if img is not None:
                print(img.shape, filename)
                h, w, c = img.shape
                fin = open(inputFolder+filename.replace('.jpg', '.txt'), 'r')
                fout = open(outputFolder+filename.replace('.jpg', '.txt'), 'w')
                
                entry = fin.readline().split(sep='\t')
                while len(entry) == 6:
                    fout.write('0\t')
                    center_x = (int(entry[1]) + int(entry[3])/2)/w
                    center_y = (int(entry[2]) + int(entry[4])/2)/h
                    width =  int(entry[3])/w
                    height = int(entry[4])/h
                    fout.write(str(center_x)+'\t'+str(center_y)+'\t'+str(width)+'\t'+str(height)+'\n')
                    print(str(center_x)+'\t'+str(center_y)+'\t'+str(width)+'\t'+str(height))
                    entry = fin.readline().split(sep='\t')
                
            # cv2.imwrite("test", img)
            # cv2.waitKey(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='/raw', help='source')  # file/folder, 0 for webcam
    parser.add_argument('--output', type=str, default='/preprocessed', help='output folder')  # output folder
    opt = parser.parse_args()

    dataPreprocessing()
    