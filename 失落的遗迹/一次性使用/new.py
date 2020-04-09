import sqlite3
import datetime

def getYesterday():
   today=datetime.date.today()
   oneday=datetime.timedelta(days=1)
   yesterday=today-oneday
   return yesterday


conn = sqlite3.connect('EndlessRiver.db')
cur = conn.cursor()

#contract = 'MA1909'
#use_date = datetime.datetime.strptime('2019-05-16', "%Y-%m-%d")
#cur.execute('''SELECT close FROM FutureInformation WHERE Contract = (?) and Date = (?)''', (contract, use_date))
#close_price = cur.fetchall()
##print(close_price)
#while close_price == []:
#    use_date -= datetime.timedelta(days=1)
#    use_date1 = str(use_date).split(' ')[0]
#    #use_date = datetime.datetime.strptime(use_date1,"%Y-%m-%d")
#    #print(use_date1)
#    cur.execute('''SELECT close FROM FutureInformation WHERE Contract = (?) and Date = (?)''', (contract, use_date1))
#    close_price = cur.fetchall()
#print(close_price[0][0])

def history_close_price(contract, use_date):
    use_date = datetime.datetime.strptime(use_date, "%Y-%m-%d")
    use_date1 = str(use_date).split(' ')[0]
    cur.execute('''SELECT close FROM FutureInformation WHERE Contract = (?) and Date = (?)''', (contract, use_date1))
    close_price = cur.fetchall()
    # print(close_price)
    while close_price == []:
        use_date -= datetime.timedelta(days=1)
        use_date1 = str(use_date).split(' ')[0]
        # use_date = datetime.datetime.strptime(use_date1,"%Y-%m-%d")
        # print(use_date1)
        cur.execute('''SELECT close FROM FutureInformation WHERE Contract = (?) and Date = (?)''',
                    (contract, use_date1))
        close_price = cur.fetchall()
    close_price = close_price[0][0]
    print(contract)
    print(str(close_price))
    return close_price

history_close_price('I1909','2019-06-06')