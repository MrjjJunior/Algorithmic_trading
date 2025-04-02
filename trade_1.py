import pandas as pd
import yfinance as yf

sp500 = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')

#sp500['Symbol'] = sp500['Symbol'].str.replace('.','-')

sp500_companies = sp500[0]

symbols = sp500_companies['Symbol'].str.replace('.', '-')

##print(symbols)

end_date = '2025-04-01'  # Date to end analyzing the company

start_date = pd.to_datetime(end_date)-pd.DateOffset(365*8)

##print(start_date)

downloadFunction = yf.download(tickers=symbols,
                               start=start_date,
                               end=end_date)

print(downloadFunction)
