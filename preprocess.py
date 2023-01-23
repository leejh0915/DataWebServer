import cv2
import base64
import io

import numpy as np
from PIL import Image

def image_encode(src, b64_mode=False):
    retval, ecd = cv2.imencode('.jpg', src) #retval : 압축결과(T/F), ecd 인코딩 이미지
    if b64_mode:
        dst = base64.b64encode(ecd[1]).decode('utf-8')
    else:
        dst = ecd
    return dst

def image_decode(src, b64_mode=False):
    if b64_mode:
        imgdata = base64.b64decode(src)
        dataByteIO = io.BytesIO(imgdata)
        img = Image.open(dataByteIO)
        dst = cv2.cvtColor(np.array((img)),cv2.COLOR_BGR2RGB)
    else:
        dst = cv2.imdecode(src, 1)
    return dst

def img_resize(src, imgsz=(640, 640)):
    dst = cv2.resize(src, imgsz)
    return dst