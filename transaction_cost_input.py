import sqlite3
import re
import requests


###用户输入部分(合约标的信息输入）
def transaction_cost_input():
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()

    commodity_name = input('请输入合约种类(比如AG): ')
    commodity_transaction_cost = float(input('请输入合约手续费标准: '))
    commodity_leverage = int(input('请输入合约杠杆: '))
    commodity_MarginRequirement = float(input('请输入合约保证金比例：'))

    decision = str('No')
    while decision != 'YES':
        print('请检查数据：')
        print('合约种类：' + commodity_name)
        print('合约手续费：' + str(commodity_transaction_cost))
        print('合约杠杆：' + str(commodity_leverage))
        print('合约保证金比例：' + str(commodity_MarginRequirement))

        decision = input('确认无误请打YES： ')
        if decision == 'YES':
            # 录入action

            cur.execute('''INSERT OR IGNORE INTO transaction_cost (commodity_name,commodity_transaction_cost,commodity_leverage,commodity_MarginRequirement) 
            VALUES ( ? ,? ,?,?)''',
                        (commodity_name, commodity_transaction_cost, commodity_leverage, commodity_MarginRequirement))
            conn.commit()

            print('录入数据完成： ' + commodity_name + str(commodity_transaction_cost) + str(commodity_leverage) + str(
                commodity_MarginRequirement))
            break
        else:
            commodity_name = input('请输入合约种类(比如AG): ')
            commodity_transaction_cost = float(input('请输入合约手续费标准: '))
            commodity_leverage = int(input('请输入合约杠杆: '))
            commodity_MarginRequirement = float(input('请输入合约保证金比例：'))