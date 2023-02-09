# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 22:24:07 2023

@author: hp
"""
import pandas as pd;

#reading file

data = pd.read_csv('transaction.csv',sep=';');


#Summary of the data


data.info()

#Mathematical Calculation
#costpertransaction

CostPerItem = data['CostPerItem'];
NumberOfItemsPurchased = data['NumberOfItemsPurchased'];
CostPerTransaction = CostPerItem * NumberOfItemsPurchased;

#adding a new column to dataframe
data['CostPerTransaction'] = CostPerTransaction;

#sales per transaction
data['SalesPerTransaction'] = data['SellingPricePerItem'] * data['NumberOfItemsPurchased'];


#profitPerTransaction 

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction'];

#Markup

data['Markup'] = data['ProfitPerTransaction'] / data['CostPerTransaction'] ;

#Rounding Markup

data['Markup'] = round(data['Markup'],2);


#Date

data['date'] = data['Day'].astype(str)  + '-' + data['Month'] + '-' + data['Year'].astype(str);

#using split

split = data['ClientKeywords'].str.split(',' , expand = True);

data['ClientAge'] = split[0].str.split("'" , expand = True)[1];
data['ClientType'] = split[1].str.split("'" , expand = True)[1];
data['LengthOfContract'] = split[2].str.split("'" , expand = True)[1];


#using the lowercase


data['ItemDescription']=data['ItemDescription'].str.lower()



#joining with the seasons 
# bnringing new data sets

seasons_data = pd.read_csv('value_inc_seasons.csv' , sep = ';')

data = pd.merge(data , seasons_data , on = 'Month');  





#dropping columns

data = data.drop('ClientKeywords' , axis = 1)
data = data.drop( ['Year' , 'Month' , 'Day'] , axis = 1)



#exporting
data.to_csv('value_inc_cleaned.csv' , index = False)




























