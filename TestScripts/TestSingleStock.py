
# Source: https://algotrading101.com/learn/yahoo-finance-api-guide/

import yfinance as yf

stock = yf.Ticker('DAI.DE')

from yahoo_fin.stock_info import get_data
import yahoo_fin.stock_info as si

ticker_list = ['ADS.DE', 'ALV.DE', 'BAS.DE']

historical_datas = {}
fundamentals = {}

for ticker in ticker_list:
    historical_datas[ticker] = get_data(ticker)
    fundamentals[ticker] = si.get_stats_valuation(ticker)

import requests
url = 'https://api.openfigi.com/v1/mapping'
headers = {'Content-Type':'text/json', 'X-OPENFIGI-APIKEY':'myKey' }
payload = '[{"idType":"ID_ISIN","idValue":"DK0060534915"}]'

r = requests.post(url, headers=headers, data=payload)