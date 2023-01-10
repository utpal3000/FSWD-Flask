# importing the library
from bs4 import BeautifulSoup
from urllib import request
import sqlite3
import traceback
import sys
from datetime import date
from datetime import datetime
   
sqliteConnection = sqlite3.connect('ex1')
cursor = sqliteConnection.cursor()
# print("Successfully Connected to SQLite")

 
# Initializing variable
url = "https://www.bankofalbania.org/Markets/Official_exchange_rate/"
fer = BeautifulSoup(request.urlopen(url).read(),'html.parser')
 
# Extracting data for article section
bodyHtml = fer.find('div', {'class' : 'mb-2'})
bodyTable = fer.find('table',{'class' : 'table'})
 
# Calculating result
res = bodyHtml.get_text()
tdata = bodyTable.get_text()

# Printing the result
udate=res[13:23]


date_object = datetime.strptime(udate, '%d.%m.%Y').date()
# print(type(date_object))
# print(date_object)  # printed in default format

today = date.today()

d1 = today.strftime("%d/%m/%Y")
sysdate = datetime.strptime(d1, '%d/%m/%Y').date()

if sysdate > date_object:
    print("Not Updated!")
else:
    print("Updated!")

print("Date on Website: ",udate)
print("Today\'s date: ",sysdate)

clst = tdata.split()
eur = clst[15]
usd = clst[11]

eur = float(eur)
usd = float(usd)
print("USD :",usd," EUR:",eur)

# # Queries to INSERT records.
cursor.execute("INSERT INTO currate (usd, eur) values (?, ?)",(usd, eur))

# cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam', '8th', 'B')''')
# cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao', '9th', 'C')''')
  
# Display data inserted
# print("Data Inserted in the table: ")
# data=cursor.execute('''SELECT * FROM currate''')
# for row in data:
#     print(row)
  
# Commit your changes in the database    
sqliteConnection.commit()
  
# Closing the connection
sqliteConnection.close()
