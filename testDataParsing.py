import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
from keras.datasets import mnist
import scipy.io as scio

# X_data = np.random.rand(200)
# # # print(X_data)
# # # print(type(X_data))
# # # print("数组的均值是：%d"%(np.mean(X_data)))
# # # print("数组的方差是：%d"%(np.var(X_data)))
# (train_images,train_labels),(test_images,test_lable) = mnist.load_data()
# print(train_images.shape)
# print(train_labels.shape)
# for i in train_labels:
#     # print(i)
#     print(type(i))
# for ii in train_images:
#     print(ii.ndim)
#     break
# print(train_images.ndim)
