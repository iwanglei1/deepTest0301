import numpy as np
import matplotlib.pyplot as plt
import someFunction as sF

moisture,d5,dp5,dp6 = sF.getOdata()
test_data,test_lable,train_data,train_lable = sF.getTestData(moisture,d5,dp5,dp6 )

ceshi_shujv = np.load('yuanshishujv.npy')
xunlian_shujv = np.load('xunlianji.npy')

rmsec = sF.calculate_RMSE(xunlian_shujv,train_lable) ## 训练集上的RMSE
rmsep = sF.calculate_RMSE(ceshi_shujv,test_lable)  ## 测试集上的RMSE

print("Root Mean Square Error of Calibrationh is : %g"%(rmsec))
print("Root Mean Square Error of Prediction is : %g"%(rmsep))
