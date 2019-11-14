import requests
from bokeh.models import tickers
from bs4 import BeautifulSoup
import pandas as pd

resp = requests.get('http://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
soup = BeautifulSoup(resp.text, 'lxml')
dfrussel = pd.read_csv('C:/Users/sofus/Documents/GitHub/investing/Data/iShares-Russell-3000-ETF_fund.csv', index_col='Symbol')


for row in table.findAll('tr')[1:]:
    ticker = row.findAll('td')[0].text
    security = row.findAll('td')[1].text
    gics_industry = row.findAll('td')[3].text
    gics_sub_industry = row.findAll('td')[4].text

    tickers.append(ticker.lower().replace(r"\n", " "))
    securities.append(security)
    gics_industries.append(gics_industry.lower())
    gics_sub_industries.append(gics_sub_industry.lower())

    # Create a list of dict based on tickers and labels
    dictlist = []
    for index, row in stocks_info_df.iterrows():
        dictlist.append({'value': row['tickers'], 'label': row['labels']})
    return dictlist

# self append
def save_self_stocks_info():
    print("Adding own list of stocks info")

    dictlist = []

    dictlist.append({'value':'sq', 'label':'SQ Square SA'})
    dictlist.append({'value':'kbsty', 'label':'Kobe steel'})
    dictlist.append({'value':'NESN', 'label':'Nestle'})
    dictlist.append({'value':'BN', 'label':'Danone'})