from keras import layers
from keras import models
import numpy as np
import matplotlib.pyplot as plt
import keras
import someFunction as sF
from keras.models import load_model


model = load_model('my_model.h5')
chengfenshui,d5,dp5,dp6 = sF.getOdata()   #调用函数返回原始数据，数据已处理为均值为零，方差为1
test_data,test_label = sF.getTestData(chengfenshui,d5,dp5,dp6)
result = model.predict(test_data)
print(result)