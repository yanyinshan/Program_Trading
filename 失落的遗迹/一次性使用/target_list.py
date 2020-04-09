import datetime
import sqlite3

#每日持仓

def getEveryDay(begin_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.today()
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list

date_list = getEveryDay('2018-12-20')
#print(date_list)
for each in date_list:
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()

    # target 是需要查找的合约
    # 0:id/1:date/2:price/3:buysell/4:contractname/5:quantity/6:type/7:transactioncost

    cur.execute('''SELECT * FROM transaction_ WHERE date_ < (?) or date_ = (?)''',(each,each))
    record = cur.fetchall()

    target = []
    print('日期  '+ each)
    for z in record:
        if z[4] not in target:
            #收集所有的合约[‘MA1909','RM1909']
            target.append(z[4])

    for target_u in target:
        count = 0
        for i in record:

            if target_u == i[4]:
                if i[3] == 1:
                    count = count + i[5] * 1
                elif i[3] == 2:
                    count = count + i[5] * -1
        if count > 0:
            print(target_u +": "+ str(count))



