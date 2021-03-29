import regulating_Hyperparameter as aU
import numpy as np

lunshu = 150
rec_rmsep = np.empty(lunshu,dtype=float)
for i in range(lunshu):
   rec_rmsep[i] = aU.au_Exp()

rec_min = np.min(rec_rmsep)
print('训练了%d轮，最小的RMSEP是：%f'%(lunshu,rec_min))
