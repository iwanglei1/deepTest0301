import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
import scipy.io as scio
from keras import layers
from keras import models
from keras.optimizers import RMSprop
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
    # print("######################################################")
    #
    # print(type(dataContAll))
    #
    # print("######################################################")
    for i in dataContAll:                                               #TODO 此处重写方便返回四种成分
         moisture[changdu] = i[0]
         changdu = changdu + 1
    data5 -= data5.mean(axis=0)  # 将数据压缩到0-1之间
    data5 /= data5.std(axis=0)
    datap5 -= datap5.mean(axis=0)
    datap5 /= datap5.std(axis=0)
    datap6 -= datap6.mean(axis=0)
    datap6 /= datap6.std(axis=0)
    return moisture,data5,datap5,datap6

chengfenshui,d5,dp5,dp6 = getOdata()   #调用函数返回原始数据，数据已处理为均值为零，方差为1
##################################################################################################
train_data = d5[:60]
test_data = d5[60:]
train_lable = chengfenshui[0:60]
test_lable  = chengfenshui[60:80]

train_data= train_data.astype('float32')
test_data= test_data.astype('float32')
train_lable = train_lable.astype('float32')
test_lable = test_lable.astype('float32')
train_data = train_data.reshape(60,700,1)
test_data = test_data.reshape(20,700,1)
# print(test_data.shape)
# test_data =test_data.reshape(80,700,1)
#################################################################################################
model = models.Sequential()
model.add(layers.Conv1D(64,5,activation='tanh',input_shape=(700,1)))
model.add(layers.MaxPooling1D(3))

model.add(layers.Conv1D(32,5,activation='tanh'))
model.add(layers.MaxPooling1D(3))

model.add(layers.Conv1D(32,5,activation='tanh'))
model.add(layers.GlobalMaxPooling1D())

model.add(layers.Dense(8))
model.add(layers.Dense(4))
model.add(layers.Dense(1))

model.summary()
model.compile(optimizer=RMSprop(),loss='mse')
history = model.fit(train_data,train_lable,epochs=20,batch_size=20,validation_data=(test_data,test_lable))
