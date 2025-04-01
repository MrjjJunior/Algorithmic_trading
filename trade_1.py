import pandas as pd


table_of_companies = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')


print(table_of_companies)
