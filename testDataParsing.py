import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
import scipy.io as scio
# 成功将需要的数据转换为矩阵
dataFile = 'C://Users//Liangyi//Desktop//'
dataName = 'corn.mat'
data = scio.loadmat(dataFile+dataName)
# for i in data:
#     print(i)
# print(data['m5spec'])
# for m5 in data['m5spec']:
#     print(m5)
# print(data['m5spec'])
# print(type(data['m5spec']))
# print(data['m5spec'].data)
datastr5 = data['m5spec']
datastr5p = data['mp5spec']
datastr6p = data['mp6spec']
dataAll = data['propvals']
# print(datast5r.shape)
# print(datastr5.size)
# print(datastr5[0,0]['data'])         #成功
data5 = datastr5[0,0]['data']
datap5 = datastr5p[0,0]['data']
datap6 = datastr6p[0,0]['data']
dataContAll = dataAll[0,0]['data']
print("######################################################")
print(data5)
print("######################################################")
print(datap5)
print("######################################################")
print(datap6)
print("######################################################")
print(dataContAll)
print("######################################################")