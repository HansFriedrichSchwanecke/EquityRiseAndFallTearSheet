import pandas as pd
import yfinance as yf

url = 'ftp://ftp.nasdaqtrader.com/SymbolDirectory/nasdaqlisted.txt'
sep = "|"


df = pd.read_csv(url, sep=sep)

movementlist = []

for stock in df.Symbol:
    yahoo_hist = yf.Ticker(stock)
    history = yahoo_hist.history(period='5d')

    low = float(1e4)
    high = 0

    for day in history.itertuples(index=True, name='Pandas'):
        if day.Low < low:
            low = day.Low
        if day.High > high:
            high = day.High

        delta = 100* (high-low) / low

    recomm = yahoo_hist.recommendations#
    bs = yahoo_hist.balancesheet
    fin = yahoo_hist.financials
    bs2 = yahoo_hist.balance_sheet
