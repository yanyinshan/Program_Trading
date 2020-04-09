import requests


url = "http://vip.stock.finance.sina.com.cn/q/view/vFutures_History.php?jys=czce&pz=MA&hy=MA1809&breed=MA1809&type=inner&start=2018-04-09&end=2018-05-09"

response = requests.get(url)

#显示乱码
#print(response.text)

response.encoding = 'gb2312'
#print(response.text)
with open('sinatest.html','w',encoding='gb2312')as f:
    f.write(response.text)

