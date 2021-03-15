import scipy.io as scio
import numpy as np
import matplotlib.pyplot as plt


################################################################################
### 从桌面上的mat文件中读取数据，然后将数据处理成均值为0，标准差为1的形式
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
def drawAcc(history):
########################################################################################################
# 绘制训练精度以及验证精度
    history_dict = history.history
    acc = history_dict['binary_accuracy']
    val_acc = history_dict['val_binary_accuracy']
    epochs = range(1, len(acc) + 1)
    plt.plot(epochs,acc,'bo',label='Training acc')
    plt.plot(epochs,val_acc,'b',label='Validation acc')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()

########################################################################################################
def drawLoss(history):
    ## 绘制训练损失和验证损失
    history_dict = history.history
    loss_values = history_dict['loss']
    val_loss_valuse = history_dict['val_loss']
    epochs = range(1, len(loss_values) + 1)
    plt.plot(epochs, loss_values, 'bo', label='Train loss')
    plt.plot(epochs, val_loss_valuse, 'b', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
#########################################################################################################
