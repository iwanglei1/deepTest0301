import datetime
import pandas as pd
from openpyxl import load_workbook
# now = datetime.datetime.now()
#
# print(type(now))
# print(now.strftime("%Y-%m-%d_%H:%M:%S")+'_'+'my_model.h5')
# print(type(now.strftime("%Y-%m-%d %H:%M:%S")))


result2=[('d5','dan bai zhi','#####','#####','####','####','####')]#需要新写入的数据
# result2=[(now_s,epochs_au,batch_size_au,rmsec,r_2_t,rmsep,r_2_p)]#需要新写入的数据
df = pd.DataFrame(result2,columns=['model_name','epochs','batch_size','RMSEC','R_C','RMSEP','R_P'])#列表数据转为数据框
df.to_csv('shiyanshujv.csv',mode='a',index=False,header=False)