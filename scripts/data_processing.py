import pandas as pd
from data_load import companies, stocks_500, index_500


#drop empty values

companies_new = companies.dropna()
stocks_new = stocks_500.dropna()
index_new = index_500.dropna()

#drop duplicates 

companies_new = companies_new.drop_duplicates()
stocks_new = stocks_new.drop_duplicates()
index_new = index_new.drop_duplicates()

#fix column names

new_company_columns = {
    'Shortname': 'Short_Name',
    'Longname' : 'Long_Name',
    'Currentprice' : 'Current_Price',
    'Ebitda': 'EBITDA',
    'Revenuegrowth' : 'Revenue_Growth',
    'Fulltimeemployees' : 'Fulltime_Employees',
    'Longbusinesssummary' : 'Business_Summary'
}

companies_new.rename(columns=new_company_columns, 
                     inplace= True)

#changing employee type from float to int

companies_new['Fulltime_Employees'] = companies_new['Fulltime_Employees'].astype(int)


companies_new.to_excel('cleaned_companies.xlsx', index = False, sheet_name= 'Companies Data')

stocks_new.to_csv('cleaned_stocks.csv', index = False)

index_new.to_excel('cleaned_index.xlsx', index = False, sheet_name= 'Index Data')




