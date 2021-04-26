import scipy.io as scio
import numpy as np


def getOdateblood():
    dataFile = 'C://Users//Liangyi//Desktop//'
    dataName = 'IDRCShootOut2010Reflect.mat'

    datablood_train = np.empty(173, dtype=float)
    datablood_test = np.empty(58, dtype=float)
    dataBloodLengthTrain = 0
    dataBloodLengthTest = 0
    data = scio.loadmat(dataFile + dataName)
    dataspecimen_train = data['XcalReflect']
    dataspecimen_test = data['XvalReflect']
    dataprop_train = data['YcalReflect']
    dataprop_test = data['YvalReflect']

    for i in dataprop_train:
        datablood_train[dataBloodLengthTrain] = i[0]
        dataBloodLengthTrain = dataBloodLengthTrain + 1

    for ii in dataprop_test:
        datablood_test[dataBloodLengthTest] = ii[0]
        dataBloodLengthTest = dataBloodLengthTest + 1

    dataspecimen_train -= dataspecimen_train.mean(axis=0)
    dataspecimen_test -= dataspecimen_test.mean(axis=0)
    dataspecimen_train /= dataspecimen_train.std(axis=0)
    dataspecimen_test /= dataspecimen_test.std(axis=0)
    dataspecimen_train = dataspecimen_train.astype('float32')
    dataspecimen_test = dataspecimen_test.astype('float32')
    datablood_train = datablood_train.astype('float32')
    datablood_test = datablood_test.astype('float32')
    dataspecimen_train = dataspecimen_train.reshape(173,700,1)
    dataspecimen_test = dataspecimen_test.reshape(58,700,1)

    return dataspecimen_test,datablood_test,dataspecimen_train,datablood_train














if __name__ == '__main__':
    getOdateblood()






