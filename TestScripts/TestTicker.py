import pandas as pd

dax = 'https://en.wikipedia.org/wiki/DAX' #3 #Ticker symbol
mdax = 'https://en.wikipedia.org/wiki/MDAX' # 1 #Symbol

index_wiki = pd.read_html(mdax)
index_constituents = index_wiki[1]

index_symbols = index_constituents['Symbol']
