import matplotlib

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pandas as pd
from skimage.data import page

from skimage.filters import (threshold_otsu, threshold_niblack,threshold_sauvola)


matplotlib.rcParams['font.size'] = 9


image = mpimg.imread('ss.jpg')
########################################################写入
binary_global = image > threshold_otsu(image)
print(type(binary_global))
data = pd.DataFrame(binary_global)
write = pd.ExcelWriter('ss.xlsx')
data.to_excel(write,'page_1',float_format='%0.5f')
write.save()
write.close()
##############################
window_size = 25

thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)

thresh_sauvola = threshold_sauvola(image, window_size=window_size)


binary_niblack = image > thresh_niblack

binary_sauvola = image > thresh_sauvola


plt.figure(figsize=(8, 7))

plt.subplot(2, 2, 1)

plt.imshow(image, cmap=plt.cm.gray)

plt.title('Original')

plt.axis('off')


plt.subplot(2, 2, 2)

plt.title('Global Threshold')

plt.imshow(binary_global, cmap=plt.cm.gray)

plt.axis('off')


plt.subplot(2, 2, 3)

plt.imshow(binary_niblack, cmap=plt.cm.gray)

plt.title('Niblack Threshold')

plt.axis('off')


plt.subplot(2, 2, 4)

plt.imshow(binary_sauvola, cmap=plt.cm.gray)

plt.title('Sauvola Threshold')

plt.axis('off')


plt.show()
