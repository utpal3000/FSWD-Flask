import sqlite3
import traceback
import sys
from datetime import date
from datetime import datetime

sqliteConnection = sqlite3.connect('FixedExhangeRate.db')
cursor = sqliteConnection.cursor()
print("Successfully Connected to SQLite")

usd = 100
eur = 112
sdate = '10/01/2022'

date = datetime.strptime(sdate, '%d/%m/%Y').date()
# # Queries to INSERT records.
#cursor.execute("create table currency_t(USD integer, EUR integer, Date date)")
cursor.execute("INSERT INTO Currency_t (usd, eur, date) values (?, ?, ?)",(usd, eur, date))


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
