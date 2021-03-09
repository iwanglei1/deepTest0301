import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
import scipy.io as scio
# 成功将需要的数据转换为矩阵
def getOdata():
    dataFile = 'C://Users//Liangyi//Desktop//'
    dataName = 'corn.mat'
    data = scio.loadmat(dataFile+dataName)

    datastr5 = data['m5spec']
    datastr5p = data['mp5spec']
    datastr6p = data['mp6spec']
    dataAll = data['propvals']
# print(datastr5[0,0]['data'])         #成功
    data5 = datastr5[0,0]['data']
    datap5 = datastr5p[0,0]['data']
    datap6 = datastr6p[0,0]['data']
    dataContAll = dataAll[0,0]['data']
    moisture = np.empty(80,dtype=float)
    changdu = 0
    print("######################################################")

    print(type(dataContAll))

    print("######################################################")
    for i in dataContAll:                                               #TODO 此处重写方便返回四种成分
         moisture[changdu] = i[0]
         changdu = changdu + 1

    return moisture,data5,datap5,datap6
chengfen,d5,dp5,dp6 = getOdata()
