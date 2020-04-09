from lxml import etree
from lxml import html
import re
import sqlite3
import requests

conn = sqlite3.connect('EndlessRiver.db')
cur = conn.cursor()

#已经完成只需要输入几个参数，就能在sina上面获取数据，并导入数据库
def userEnter(contract, startdate, enddate):

    url = "http://vip.stock.finance.sina.com.cn/q/view/vFutures_History.php?jys=czce&pz=MA&hy=MA1909&breed=" +contract + "&type=inner&start=" + startdate +"&end=" +enddate
    return url

def findAll_url(url):
    response = requests.get(url)

    # 显示乱码
    # print(response.text)

    response.encoding = 'gb2312'
    # print(response.text)
    with open('sinatest.html', 'w', encoding='gb2312')as f:
        f.write(response.text)

    with open('sinatest.html', 'r')as a:
        contend = a.read()

    tree = etree.HTML(contend)
    for link in tree.xpath("//div[@class = 'historyList']//@href"):
    print(link)
    print('1')
    url_list = tree.xpath("//div[@class = 'historyList']//@href")
    numpage = re.findall('page=(\d)', url_list[len(url_list) - 2]).pop()
    # print(numpage)
    num = 1
    for each in range(int(numpage) - 1):
        num += 1
        print(num)


#如果有更多的信息继续查找
def enter_intoDB():

    response = requests.get(url)

    # 显示乱码
    # print(response.text)

    response.encoding = 'gb2312'
    # print(response.text)
    with open('sinatest.html', 'w', encoding='gb2312')as f:
        f.write(response.text)

    with open('sinatest.html', 'r')as a:
        contend = a.read()
        # print(contend)

    tree = etree.HTML(contend)

    tablerow = tree.xpath("//div[@class = 'historyList']")[0]

    pattern_atribute = re.compile('<.*?>')
    pattern_atribute2 = re.compile('(#\d+)')

    text = str(etree.tostring(tablerow))
    text2 = pattern_atribute.sub('', text)
    text2 = pattern_atribute2.sub('', text2)
    #print(text2)
    contractName = re.findall('\(([A-Z]+\d+)\)', text2)[0]
    # print(re.findall('t(\d+\-\d+\-\d+)',text2))
    # print(re.findall('t(\d+)',text2))
    dateList = re.findall('t(\d+\-\d+\-\d+)', text2)
    # print(dateList)
    numOfDate = 0
    for each in dateList:
        numOfDate += 1
    print(numOfDate)

    dataOfTarget = re.findall('t(\d+)', text2)
    dataOfTarget.reverse()
    numOfData = 0
    for i in dataOfTarget:
        numOfData += 1
    print(numOfData)

    for each in dateList:
        enter_list = []
        IDcode = contractName + each
        enter_list.append(IDcode)
        enter_list.append(contractName)
        enter_list.append(each)

        # ['MA1909','2019-04-09']
        order = 0
        for i in range(6):
            order += 1
            if order < 2:
                dataOfTarget.pop()
            else:
                enter_list.append(dataOfTarget.pop())
        cur.execute('''INSERT OR replace INTO FutureInformation VALUES(?,?,?,?,?,?,?,?)''', (
            enter_list[0], enter_list[1], enter_list[2], enter_list[3], enter_list[4], enter_list[5], enter_list[6],
            enter_list[7]))
        conn.commit()

        print(enter_list)

#print(text2)


