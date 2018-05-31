from datetime import datetime
import time
from xlrd import xldate_as_tuple
import numpy as np
import matplotlib.pyplot as plt
from xlwt import Workbook

import  xdrlib ,sys
import xlrd
workbook = xlrd.open_workbook('C:\\Users\\Administrator\\Desktop\\Y4\\FYP\\结果\\backtesting_55_volatile.xls')
worksheets = workbook.sheet_names()
#print('worksheets is %s' %worksheets)
table = workbook.sheets()[0]
btc=table.col_values(3)
gs=table.col_values(2)
date=table.col_values(4)
#time_local=time.localtime(date)
#dt=time.strftime("%Y-%m-%d %H:%M:%S",time_local)
#date = table.cell(i,4).value
#date = datetime(*xldate_as_tuple(i, 0))
plt.title('Grid Strategy Returns in volatile market (20150110-20150718)')
plt.xlabel('Date')
plt.ylabel('Returns')
#plt.plot(x1, y1,'r', label='broadcast')
#plt.plot(x2, y2,'b',label='join')
#plt.xticks(x1, group_labels, rotation=0)
x3=date
x4=date
y3=gs
y4=btc
plt.plot(x3, y3,'r', label='Grid Strategy')
plt.plot(x4, y4,'b',label='BTC Index')
#plt.xticks(x3, date, rotation=0)
plt.legend(bbox_to_anchor=[0.3, 1])
plt.grid()
plt.show()
