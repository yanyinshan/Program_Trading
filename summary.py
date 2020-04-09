import sqlite3
import re
import Unsettled_Transaction as ut
import SettledPL as sp

import requests

def summary():
    # contract_list 是需要查找的合约
    # 0:id/1:date/2:price/3:buysell/4:contractname/5:quantity/6:type/7:transactioncost
    conn = sqlite3.connect('EndlessRiver.db')
    cur = conn.cursor()

    cur.execute('''SELECT * FROM transaction_''')
    records = cur.fetchall()

    # 收集交易过的所有合约的名字
    contract_list = []
    for z in records:
        if z[4] not in contract_list:
            contract_list.append(z[4])
    pl2 = []
    pl3 = 0
    for contract in contract_list:

        pl =sp.build_settled_profit(
            sp.build_settled_quantity(contract),
            sp.build_account_priceup(contract),
            sp.build_account_pricedown(contract),
            sp.build_leverage(contract),
            sp.build_transaction_cost(contract),
            contract
        )
        pl2.append(pl)
        pl3 = pl3 + pl2.pop()
    print('-'.center(83, "-"))
    print("|" + 'Total Settled Profit/Loss(RMB):'.center(55) + "|" + str(round(pl3, 2)).rjust(25) + "|")
    return pl3
