import sqlite3
import re
import Unsettled_Transaction as ut

def build_transaction_cost(contract):
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()
    cur.execute('''SELECT transaction_cost FROM transaction_ WHERE commodity_name =(?)''', (contract,))
    transaction_cost_list = cur.fetchall()
    transaction_cost_list2 = []
    for each in transaction_cost_list:
        transaction_cost_list2.append(list(each)[0])

    transaction_costs = 0
    for cost in transaction_cost_list2:
        transaction_costs = transaction_costs + cost
    return transaction_costs

def build_account_priceup(contract):
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()

    # target 是需要查找的合约
    # 0:id/1:date/2:price/3:buysell/4:contractname/5:quantity/6:type/7:transactioncost
    cur.execute('''SELECT * FROM transaction_ WHERE commodity_name =(?)''', (contract,))
    record = cur.fetchall()

    quantity_list = []
    account_priceup = []
    account_pricedown = []
    quantity = 0
    for i in record:
        if int(i[3]) == 1 and int(i[5]) == 1:
            account_priceup.append(i[2])
            quantity_list.append(1)
            quantity = quantity + 1
        elif int(i[3]) != 1 and int(i[5]) == 1:
            account_pricedown.append(int(i[2] * -1))
            quantity_list.append(1)
            quantity = quantity - 1
        elif int(i[3]) == 1 and int(i[5]) != 1:
            for num in range(int(i[5])):
                account_priceup.append(i[2])
                quantity_list.append(1)
                quantity = quantity + 1
        elif int(i[3]) != 1 and int(i[5]) != 1:
            temp_num = int(i[2]) * -1
            for num in range(int(i[5])):
                account_pricedown.append(temp_num)
                quantity_list.append(1)
                quantity = quantity - 1

    return account_priceup

def build_account_pricedown(contract):
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()

    # target 是需要查找的合约
    # 0:id/1:date/2:price/3:buysell/4:contractname/5:quantity/6:type/7:transactioncost
    cur.execute('''SELECT * FROM transaction_ WHERE commodity_name =(?)''', (contract,))
    record = cur.fetchall()

    quantity_list = []
    account_priceup = []
    account_pricedown = []
    quantity = 0
    for i in record:
        if int(i[3]) == 1 and int(i[5]) == 1:
            account_priceup.append(i[2])
            quantity_list.append(1)
            quantity = quantity + 1
        elif int(i[3]) != 1 and int(i[5]) == 1:
            account_pricedown.append((i[2] * -1))
            quantity_list.append(1)
            quantity = quantity - 1
        elif int(i[3]) == 1 and int(i[5]) != 1:
            for num in range(int(i[5])):
                account_priceup.append(i[2])
                quantity_list.append(1)
                quantity = quantity + 1
        elif int(i[3]) != 1 and int(i[5]) != 1:
            temp_num = (i[2]) * -1
            for num in range(int(i[5])):
                account_pricedown.append(temp_num)
                quantity_list.append(1)
                quantity = quantity - 1

    return account_pricedown

def build_settled_quantity(contract):
    settled_quantity = min(len(ut.build_account_priceup(contract)),len(ut.build_account_pricedown(contract)))
    return settled_quantity

def build_leverage(contract):
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()
    ticker = re.findall(('[A-Z]+'), contract)[0]
    cur.execute('''SELECT commodity_leverage FROM transaction_cost WHERE commodity_name =(?)''', (ticker,))
    leverage = cur.fetchone()[0]
    return leverage

def build_settled_profit(settled_quantity,account_priceup,account_pricedown,leverage,transaction_cost,contract):
    pl = 0
    account_priceup.reverse()
    account_pricedown.reverse()

    for num in range(settled_quantity):


        #print(account_priceup )
        #print(account_pricedown)
        accountup = account_priceup.pop()
        accountdown = account_pricedown.pop()
        pl = pl - (accountdown+accountup)*leverage

    pl = pl - transaction_cost
    pl = round(pl,2)

    print("|" + contract.center(20) + "|" + str(pl).center(60) + "|")

    return pl







