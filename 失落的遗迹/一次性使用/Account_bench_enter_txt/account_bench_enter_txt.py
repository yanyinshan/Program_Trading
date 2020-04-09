import sqlite3
conn = sqlite3.connect('EndlessRiver.db')
cur = conn.cursor()

#以类编译的获取净值分母的程序
class BookValue():
    def __init__(self,date,cash,stock,public_fund,futures,loan):
        self.date = date
        self.cash = cash
        self.stock = stock
        self.public_fund = public_fund
        self.futures = futures
        self.loan = loan

    def __str__(self):
        msg = self.date + " " + str(self.cash) + " " + str(self.stock) + " " + str(self.public_fund) + " " + str(self.futures) + " " + str(self.loan) +'\n'
        return msg

    def enterDB(self):
        cur.execute('''INSERT OR IGNORE INTO Account_Bench (Date,Cash,Stock,Public_Fund,Futures,Loan) 
            VALUES ( ? ,? ,? ,? ,? ,?  )''', (self.date, self.cash,self.stock,self.public_fund,self.futures,self.loan))
        conn.commit()
        print('完成！')

with open('transaction.txt','r') as f:
    text = f.read()
    msg = text.split('\n')


for exam in msg:
    exam = exam.split(',')
    example = BookValue(exam[0],exam[1],exam[2],exam[3],exam[4],exam[5])
    example.enterDB()
    print(exam)

