from bs4 import BeautifulSoup
import requests 
import pandas as pd
import streamlit as st

st.set_page_config(page_title="optimasi", layout="wide")

df = pd.DataFrame()

# variable global dataframe
stock_name_list = []
stock_price_list = []
stock_symbol_list = []

# link url target
url = BeautifulSoup(requests.get("https://www.tradingview.com/markets/stocks-indonesia/sectorandindustry-industry/marine-shipping/").text)

# first we should find our table object:
table = url.find('table')

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

def scrape(date):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tr = soup.find_all('tr',attrs={'class': 'row-RdUXZpkv'})
    count = 10
    for row in tr:
        if count == 10:
            break
        count = count + 1
        stock_name = row.find('th', attrs={
            'class': 'cell-seAzPAHn cell-fixed-RHkwFEqU onscroll-shadow'})
