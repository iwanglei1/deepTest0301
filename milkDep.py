import scipy.io as scio
import numpy as np


def getOdatebmilkDep():
    dataFile = 'C://Users//Liangyi//Desktop//'
    dataName = 'milkdeppp.mat'


    data = scio.loadmat(dataFile + dataName)
    dataspecimen_train = data['Xcal']
    dataspecimen_test = data['Xtest']
    dataprop_train = data['ycal']
    dataprop_test = data['ytest']



    dataspecimen_train -= dataspecimen_train.mean(axis=0)
    dataspecimen_test -= dataspecimen_test.mean(axis=0)
    dataspecimen_train /= dataspecimen_train.std(axis=0)
    dataspecimen_test /= dataspecimen_test.std(axis=0)
    dataspecimen_train = dataspecimen_train.astype('float32')
    dataspecimen_test = dataspecimen_test.astype('float32')
    dataprop_train = dataprop_train.astype('float32')
    dataprop_test = dataprop_test.astype('float32')
    dataspecimen_train = dataspecimen_train.reshape(50,1557,1)
    dataspecimen_test = dataspecimen_test.reshape(17,1557,1)

    return dataspecimen_test,dataprop_test,dataspecimen_train,dataprop_train














if __name__ == '__main__':
    getOdatebmilkDep()






