import easyocr
import cv2
reader = easyocr.Reader(['en']) # need to run only once to load model into memory
img = cv2.imread('/home/bill/alpr-insight/LPdataset/ga1484.png')
img = cv2.resize(img, (160, 80), interpolation=cv2.INTER_CUBIC)
result = reader.readtext(img, detail=0, min_size=120, allowlist='0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ')
print(result)