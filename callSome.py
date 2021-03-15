
import someFunction as sF
import someModel as sM
import tensorflow as tf

config = tf.compat.v1.ConfigProto(gpu_options=tf.compat.v1.GPUOptions(allow_growth=True))
sess = tf.compat.v1.Session(config=config)
# 成功将需要的数据转换为矩阵
### 写一个函数，从原始mat中读取需要的数据，并进行返回
chengfenshui,d5,dp5,dp6 = sF.getOdata()   #调用函数返回原始数据，数据已处理为均值为零，方差为1
##################################################################################################
#### 这里的代码准备数据
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
### 调用模型
history = sM.trainModel(train_data,train_lable,test_data,test_lable)
print(history.history.keys())
sF.drawLoss(history)
#########################################################################################################


