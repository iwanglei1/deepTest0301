# coding=utf-8
import glob
import os

from PIL import Image

# print(glob.glob(r'D:\VideoPhotos\sign\*.jpg'))
path = r'D: \VideoPhotos\sign'
images = glob.glob(path + r" \* .jpg")
for img in images:
    # print(img)
    im = Image.open(img)
    # print(im.format, im.size, im.mode)
    size = 1224, 1632
    # print(size)
    name = os.path.join(path, img)
    im.thumbnail(size)
    im.save(name, 'JPEG')
    # print(im.format, im.size, im.mode)