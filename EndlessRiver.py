import sqlite3
from transaction_input import transaction_input
from transaction_cost_input import transaction_cost_input
from position import position
from summary import summary
from unsettle_profit import unsetprofit

conn = sqlite3.connect('EndlessRiver.db')
cur = conn.cursor()

rock1 = 0
while rock1 == 0:
    print('|'+'1录入模式'.center(27) + '|'+'2查询模式'.center(27) +'|'+'3结束程序'.center(27)+'|')
    command = int(input('请输入指令： '))
    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

    if command == 1:
        print('|' + '1合约信息录入'.center(27) + '|' + '2交易信息录入'.center(27) + '|' + '3返回上层'.center(27) + '|')
        command_2 = int(input('请输入录入选项： '))
        print('\n\n')
        if command_2 == 1:
            transaction_cost_input()
            continue
        elif command_2 == 2:
            transaction_input()
            continue
        elif command_2 == 3:
            continue

    elif command == 2:
        print('|' + '1目前持仓查询'.center(27) + '|' + '2账目确定盈利情况'.center(27) + '|' + '3浮动盈亏查询'.center(27) + '|'+ '4所有盈亏总结'.center(27) + '|'+ '5返回上层'.center(27) + '|')
        command_2 = int(input('请输入录入选项： '))
        if command_2 == 1:
            position()
            continue
        elif command_2 == 2:
            print('-'.center(83, "-"))
            print("|" + 'Contract'.center(20) + "|" + 'Settled Profit'.center(60) + "|")
            summary()
            print('-'.center(83, "-"))
            continue
        elif command_2 == 3:
            print('-'.center(83, "-"))
            print("|" + 'Contract'.center(20) + "|"  + 'Unsettled profit'.center(60) + "|")
            unsetprofit()
            print('-'.center(83, "-"))
            continue
        elif command_2 == 4:
            print('-'.center(83, "-"))
            print("|" + 'Contract'.center(20) + "|" + 'Settled Profit'.center(60) + "|")

            setted = summary()
            print('-'.center(83, "-"))
            print("|" + 'Contract'.center(20) + "|" + 'Unsettled profit'.center(60) + "|")
            unsetted = unsetprofit()
            print('-'.center(83, "-"))
            print('-'.center(83, "-"))
            total = setted + unsetted
            print("|" + 'Total Profit/Loss(RMB):'.center(55) + "|" + str(round(total, 2)).rjust(25) + "|")
            print('-'.center(83, "-"))


            continue
        elif command_2 ==5:
            continue

    elif command == 3:
        print('结束')
        break
