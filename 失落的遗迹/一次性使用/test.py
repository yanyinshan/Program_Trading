import sqlite3
import datetime
conn = sqlite3.connect('EndlessRiver.db')
cur = conn.cursor()

def benchdate(real_date):
    date_list = []
    cur.execute('''SELECT Date from Account_bench''')
    text = cur.fetchall()
    for each in text:
        date_list.append(each[0])

    target_date = datetime.datetime.strptime(real_date, "%Y-%m-%d")

    position = 0
    for each in date_list:
        position += 1
        if target_date == datetime.datetime.strptime(each,'%Y-%m-%d'):
            #print(datetime.datetime.strptime(each,'%Y-%m-%d'))
            bench_date = datetime.datetime.strptime(each,'%Y-%m-%d')
        try:
            if target_date > datetime.datetime.strptime(date_list[position-1],'%Y-%m-%d') and target_date < datetime.datetime.strptime(date_list[position],'%Y-%m-%d'):
                #rint(datetime.datetime.strptime(date_list[position-1],'%Y-%m-%d'))
                bench_date = datetime.datetime.strptime(date_list[position - 1], '%Y-%m-%d')
        except:
            #print(datetime.datetime.strptime(date_list[position-1],'%Y-%m-%d'))
            bench_date = datetime.datetime.strptime(date_list[position - 1], '%Y-%m-%d')

    benchdate = str(bench_date).split(' ')[0]
    print(benchdate)
    return benchdate

x = benchdate('2019-09-28')
cur.execute('''SELECT * FROM Account_bench WHERE Date <= (?)''',(x,))
y = cur.fetchall()

#print(y)

