import sqlite3
import re
import requests

def transaction_input():
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()

    date = str(input('请输入成交时间： (YYYY-MM-DD)'))
    contract_name = str(input('请输入合约名称： (HC1905)'))
    action = str(input('请输入买卖动作： (B/S) '))
    quantity = int(input('请输入成交数量： '))
    price = float(input('请输入成交价格： '))
    type_ = str(input('请输入交易类型：'))
    contract_ = ''.join(re.findall(r'[a-zA-Z]',contract_name))
#   print(contract_)

#   transaction cost calculation
    cur.execute('''SELECT commodity_transaction_cost FROM transaction_cost WHERE commodity_name = (?) ''', (contract_,))
    transaction_cost = cur.fetchone()[0]
    if transaction_cost < 1:
        transaction_cost = round(transaction_cost*price*quantity,2)
    else:
        transaction_cost = round(transaction_cost*quantity,2)
#    print(transaction_cost)

#   Action_id
    if action == 'B':
        action_id = int(1)
    else:
        action_id = int(2)

    decision = str('No')
    while decision !='YES':
        print('请检查数据：')
        print('时间：' + date)
        print('合约名称：' + contract_name)
        print('动作：' + action)
        print('成交数量：' + str(quantity))
        print('价格：' + str(price))
        print('类型：' + type_)
        print('合约种类：' + contract_)
        decision = input('确认无误请打YES： ')
        if decision == 'YES':
            # 录入transaction
            cur.execute('''INSERT OR IGNORE INTO transaction_ (date_,price,action_id,commodity_name,quantity,type,transaction_cost) 
                        VALUES ( ? ,? ,? ,? ,? ,? ,? )''',
                        (date, price, action_id, contract_name, quantity, type_, transaction_cost))
            conn.commit()

            print('录入数据完成 ')
            break
        else:
            date = str(input('请输入成交时间： '))
            contract_name = input('请输入合约名称： ')
            action = input('请输入买卖动作(B/S)： ')
            quantity = int(input('请输入成交数量: '))
            price = float(input('请输入成交价格:'))
            type_ = str(input('请输入交易类型：'))
            contract_ = ''.join(re.findall(r'[a-zA-Z]', contract_name))
            #   print(contract_)

            #   transaction cost calculation
            cur.execute('''SELECT commodity_transaction_cost FROM transaction_cost WHERE commodity_name = (?) ''',
                        (contract_,))
            transaction_cost = cur.fetchone()[0]
            if transaction_cost < 1:
                transaction_cost = transaction_cost * price * quantity
            else:
                transaction_cost = transaction_cost * quantity
            #    print(transaction_cost)

            #   Action_id
            if action == 'B':
                action_id = int(1)
            else:
                action_id = int(2)


