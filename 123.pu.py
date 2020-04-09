print("|" + ticker.center(20) + "|" + str(round(profit, 2)).center(60) + "|")
profit2.append(profit)
for y in profit2:
    total = total + y
print('-'.center(83, "-"))
print("|" + 'Total Settled Profit/Loss(RMB):'.center(55) + "|" + str(round(total, 2)).rjust(25) + "|")