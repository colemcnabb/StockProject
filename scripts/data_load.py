
import pandas as pd
import kaggle
import zipfile

# kaggle dataset API
#!kaggle datasets download -d andrewmvd/sp-500-stocks

#extract file from download 

zip_name = 'sp-500-stocks.zip'
with zipfile.ZipFile(zip_name, 'r') as file:
    file.extractall()

#read csv files as pandas df
companies = pd.read_csv('sp500_companies.csv')
index_500 = pd.read_csv('sp500_index.csv')
stocks_500 = pd.read_csv('sp500_stocks.csv')

#exploring data

if __name__ == '__main__': 
    print('Companies DF Info:')
    companies.info()
    print('\nIndex 500 DF Info:')
    index_500.info()
    print('\nStocks DF Info:')
    stocks_500.info()