import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import time
import talib
import tushare as ts
# pip install https://github.com/matplotlib/mpl_finance/archive/master.zip

from matplotlib.pylab import date2num

# 获取上证指数数据
ts.set_token('a7e93a26377bddf7184aa2312505579ee5b403f7b0f2e14286e465cf')
pro = ts.pro_api()
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code')

ts_code='300395.SZ'
if ts_code[0:3] != "300":
    pass
time.sleep(0.13)
try:
    df1 = ts.bak_daily(ts_code=ts_code,trade_date='20200902')
    df = ts.pro_bar(ts_code=ts_code, adj='qfq', start_date='20190716', end_date='20200902', ma=[5, 10, 250])
    if len(df["open"]) < 250:
        pass
    last10Data = df[0:15]
    findflag = [0]
    for x in range(0, 14):
        findflag[0] = 1
        closevalue = last10Data["close"][x]
        ma250 = last10Data["ma250"][x]
        ma5 = last10Data["ma5"][x]
        d5value = closevalue - ma5
        d250value = closevalue - ma250
        percent5 = abs(d5value / closevalue)
        percent250 = abs(d250value / closevalue)
        if pd.isnull(d250value):
            print("ma250:" + str(d250value) + ":" + ts_code)
        if x == 0:
            if d250value > 0 or percent250 > 0.03:
                findflag.append(1)
                break
        else:
            if d250value > 0 or percent250 > 0.10 or percent5 > 0.05:
                findflag.append(1)
                break

    if sum(findflag) == 1:
        print("find one share:" + ts_code)
        with open("douban.txt", "a") as f:
            f.write("find one share:" + ts_code + "\n")
    else:
        print("not fit:" + ts_code)
except Exception as e:
    # 访问异常的错误编号和详细信息
    print(e)
    # continue

# print(last10Data)
# print(df)
