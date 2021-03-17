from keras.models import Sequential
from keras.layers import Dense
from keras import layers
from keras import models
from  keras import metrics
from keras.optimizers import RMSprop
import keras
callback_list1 =[
    keras.callbacks.ModelCheckpoint(
        filepath= 'my_model.h5',      ##文件路径 存在当前路径下吧 还好找
        monitor= 'val_loss',         ## 监控指标
        save_best_only= True        ## 保持最佳模型
    )
]
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
    history = model.fit(train_data,train_lable,
                        epochs=30,
                        batch_size=20,
                        validation_data=(test_data,test_lable),
                        callbacks= callback_list1
                        )
    return history
###########################################################################################################