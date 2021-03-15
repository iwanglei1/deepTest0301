import numpy as np
#画图
import matplotlib.pyplot as plt
#载入图片
import matplotlib.image as mpimg
import pandas as pd
#导出数组文件
import numpy as np

# a =[1,2,3,4,5,6]
# print(a)
# print(a[0:3])
# print(a[3:6])
tupian = mpimg.imread('ss.jpg')
# tupian.flags['WRITEABLE'] = True
immg = np.array(tupian)
# print(immg.flags)
# print(immg)


data = pd.DataFrame(immg)

write = pd.ExcelWriter('eee.xlsx')
data.to_excel(write,'page_1',float_format='%0.5f')
write.save()
write.close()