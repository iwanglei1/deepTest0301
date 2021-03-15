from keras.models import Sequential
from keras.layers import Dense
from keras import layers
from keras import models
from  keras import metrics
from keras.optimizers import RMSprop


####################################################################################################
def trainModel(train_data,train_lable,test_data,test_lable):
#####下面的代码进行训练 核心参数是神经网络的层数，卷积核的大小，密集层的细胞个数和层数
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
    history = model.fit(train_data,train_lable,epochs=30,batch_size=20,validation_data=(test_data,test_lable))
    return history
###########################################################################################################