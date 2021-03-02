from keras.datasets import mnist
print("不想写代码的程序员")
import numpy as np

# 将多个数组保存到磁盘
a = np.arange(5)
b = np.arange(6)
c = np.arange(7)
np.savez('test', a, b, c_array=c)  # c_array是数组c的命名
# 读取数组
data = np.load('test.npz')  #类似于字典{‘arr_0’:a,’arr_1’:b,’c_array’:c}
print('arr_0 : ', data['arr_0'])
print('arr_1 : ', data['arr_1'])
print('c_array : ', data['c_array'])

