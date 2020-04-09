import datetime

new = datetime.datetime.strptime('2019-03-21', "%Y-%m-%d") + datetime.timedelta(days=1)
print(new)
