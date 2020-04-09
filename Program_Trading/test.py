import sqlite3
import requests
import re


record = ["AG1912"]
target = []

czce_list = ["AP", "CF", "CY", "FG", "JR", "LR", "MA", "OI", "PM", "RI", "RM", "RS", "SF", "SM", "SR", "TA", "ZC",
             "WH"]
shfe_list = ["AG", "AL", "AU", "BU", "CU", "FU", "HC", "NI", "PB", "RB", "RU", "SN", "SP", "WR", "ZN"]
dce_list = ["A", "B", "BB", "C", "CS", "EG", "FB", "I", "J", "JD", "JM", "L", "M", "P", "PP", "V", "Y"]

print("|" + '合约'.center(12) + "|" + 'Ticker'.center(12) + "|" + 'Price'.center(12) + "|" + 'quantity'.center(
    12) + "|" + 'Time'.center(24) + "|")
text2=str("|" + '合约'.center(12) + "|" + 'Ticker'.center(12) + "|" + 'Price'.center(12) + "|" + 'quantity'.center(
    12) + "|" + 'Time'.center(24) + "|")
for z in record:
    if z[4] not in target:
        target.append(z[4])

for target_u in target:
    count = 0
    for i in record:

        if target_u == i[4]:
            if i[3] == 1:
                count = count + i[5] * 1
            elif i[3] == 2:
                count = count + i[5] * -1

    # 1:代码/2：合约/3:时间/4:最新价格/5:涨跌%/6:涨跌幅/7:今开/8：最高/9：成交量/10：前结/14：最低
    if count != 0:

        # print('合约：' + str(target_u) + '有' + str(count) + '手')
        ticker = re.findall(('[A-Z]+'), target_u)[0]
        if ticker in czce_list:
            kind = str(4)
            number = target_u[-3:]
            url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=" + str(ticker) + str(
                number) + str(
                kind) + "&sty=FDPBPFBTA&st=z&sr=&p=&ps=&cb=jQuery17208838746005115159_1554896968780&js=([[(x)]])&token=7bc05d0d4c3c22ef9fca8c2a912d779c&_=1554896969034"
            c = requests.get(url)
            backinf = c.text
            backinf2 = backinf.split(",")
            x2 = backinf2[2]
            x1 = backinf2[1]
            x4 = backinf2[4]
            x3 = backinf2[3]
            print("|" + x2.center(12) + "|" + x1.center(12) + "|" + x4.center(12) + "|" + str(count).center(
                12) + "|" + x3.center(24) + "|")
        elif ticker in shfe_list:
            kind = str(1)
            number = target_u[-4:]
            url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=" + str(ticker) + str(
                number) + str(
                kind) + "&sty=FDPBPFBTA&st=z&sr=&p=&ps=&cb=jQuery17208838746005115159_1554896968780&js=([[(x)]])&token=7bc05d0d4c3c22ef9fca8c2a912d779c&_=1554896969034"
            c = requests.get(url)
            backinf = c.text
            backinf2 = backinf.split(",")
            x2 = backinf2[2]
            x1 = backinf2[1]
            x4 = backinf2[4]
            x3 = backinf2[3]
            print("|" + x2.center(12) + "|" + x1.center(12) + "|" + x4.center(12) + "|" + str(count).center(
                12) + "|" + x3.center(24) + "|")

        elif ticker in dce_list:
            kind = str(3)
            number = target_u[-4:]
            url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=" + str(ticker) + str(
                number) + str(
                kind) + "&sty=FDPBPFBTA&st=z&sr=&p=&ps=&cb=jQuery17208838746005115159_1554896968780&js=([[(x)]])&token=7bc05d0d4c3c22ef9fca8c2a912d779c&_=1554896969034"
            c = requests.get(url)
            backinf = c.text
            backinf2 = backinf.split(",")
            x2 = backinf2[2]
            x1 = backinf2[1]
            x4 = backinf2[4]
            x3 = backinf2[3]
            print("|" + x2.center(12) + "|" + x1.center(12) + "|" + x4.center(12) + "|" + str(count).center(
                12) + "|" + x3.center(24) + "|")