import Unsettled_Transaction as ut


def unsetprofit():
    pl2 = []
    pl3 = 0
    for contract in ut.build_contract():
        pl = ut.build_unsettled_profit(
            ut.build_market_value(
                ut.build_quantity(contract),
                ut.build_current_price(contract),
                ut.build_leverage(contract)
            ),
            ut.build_total_cost(
                ut.build_quantity(contract),
                ut.build_account_priceup(contract),
                ut.build_account_pricedown(contract),
                ut.build_quantity_list(contract),
                ut.build_leverage(contract)
            ),
            contract)
        pl2.append(pl)
        pl3 = pl3 + pl2.pop()
    print('-'.center(83, "-"))
    print("|" + 'Total Unsettled Profit/Loss(RMB):'.center(55) + "|" + str(round(pl3, 2)).rjust(25) + "|")
    return pl3

