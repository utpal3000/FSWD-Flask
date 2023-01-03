
# importing the library
from bs4 import BeautifulSoup
from urllib import request
 
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
print(res)

clst = tdata.split()
eur = clst[15]
usd = clst[11]

eur = float(eur)
usd = float(usd)
print("USD :",usd," EUR:",eur)
