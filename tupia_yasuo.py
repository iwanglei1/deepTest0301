from PIL import Image
import os

path = "test.jpg"
im = Image.open(path)  # 返回一个Image对象

# os模块中的path目录下的getSize()方法获取文件大小，单位字节Byte
size = os.path.getsize(path) / 1024  # 计算图片大小即KB
print(size)
# size的两个参数
width, height = im.size[0], im.size[1]
# 用于保存压缩过程中的temp路径,每次压缩会被不断覆盖
newPath = 'temp.jpg'
while size > 10:
    width, height = round(width * 0.9), round(height * 0.9)
    print(width, height)
    im = im.resize((width, height), Image.ANTIALIAS)
    im.save(newPath)
    size = os.path.getsize(newPath) / 1024

# 压缩完成
im.save('Compressed.jpg')