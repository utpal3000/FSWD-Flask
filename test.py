from datetime import date
from datetime import datetime

datetime_str = '09.19.22 13:55:26'

udate = '10.01.2023'

date_str = '09-19-2022'

date_object = datetime.strptime(udate, '%d.%m.%Y').date()
# print(type(date_object))
# print(date_object)  # printed in default format

today = date.today()

d1 = today.strftime("%d/%m/%Y")
sysdate = datetime.strptime(d1, '%d/%m/%Y').date()

if sysdate > date_object:
    print("Not Updated!")
    print(sysdate)
else:
    print("updated!")
    print(date_object)