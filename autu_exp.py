import regulating_Hyperparametermilk as aU
import numpy as np

lunshu = 2
rec_rmsep = np.empty(lunshu,dtype=float)
rec_r_2_p = np.empty(lunshu,dtype=float)
for i in range(lunshu):
   rec_rmsep[i],rec_r_2_p[i] = aU.au_Exp()

rec_min = np.min(rec_rmsep)
r_2_p_max = np.max(rec_r_2_p)
print('训练了%d轮，最小的RMSEP是：%f'%(lunshu,rec_min))
print('训练了%d轮，最大的R方是：%f'%(lunshu,r_2_p_max))
