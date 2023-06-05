from bs4 import BeautifulSoup
import requests 

soup = BeautifulSoup(requests.get("https://www.tradingview.com/markets/stocks-indonesia/sectorandindustry-industry/marine-shipping/").text)
# first we should find our table object:
table = soup.find('table')
# then we can iterate through each row and extract either header or row values:
header = []
rows = []
for i, row in enumerate(table.find_all('tr')):
    if i == 0:
        header = [el.text.strip() for el in row.find_all('th')]
    else:
        rows.append([el.text.strip() for el in row.find_all('td')])

print(header)

for row in rows:
    print(row)