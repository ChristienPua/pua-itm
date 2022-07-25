from asyncio.format_helpers import extract_stack
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

with open('C:\\Users\\chris\Downloads\\transaction-data-adhoc-analysis.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)

df_january = df[df['transaction_date'].str.contains('2022/01')]
df_february = df[df['transaction_date'].str.contains('2022/02')]
df_march = df[df['transaction_date'].str.contains('2022/03')]
df_april = df[df['transaction_date'].str.contains('2022/04')]
df_may = df[df['transaction_date'].str.contains('2022/05')]
df_june = df[df['transaction_date'].str.contains('2022/06')]

#####################################################################################################################################

def spliter(items): #creates a function to clean up unwanted strings
    items_list = items.replace(',',' ').split(';')
    return items_list

df['transaction_items'] = df['transaction_items'].apply(spliter) #apply function to df transac items

fixed_items = pd.DataFrame(df['transaction_items'].tolist()) #defines fixed_items as the list of new df
fixed_items.replace('',np.nan,regex=True,inplace=True) #replaces all blank values in the df
fixed_items_row = fixed_items.melt(value_name = 'items') #melts the df and renames value_name into 'items'
fixed_items_row.drop(columns=['variable'],inplace=True) #removes the column 'variable'
fixed_items_row.dropna(axis=0,how='all',inplace=True) #removes all missing values

def items_in_depth(n):
    fixed_items_final = []
    fixed_items_final.append(n[:n.find('(')-1])
    fixed_items_final.append(int(n[n.find(')')-1]))
    return fixed_items_final

fixed_items_row['as_list'] = fixed_items_row['items'].apply(items_in_depth)
items_final_df = pd.DataFrame(fixed_items_row['as_list'].tolist(), columns=['items','quantity'])

beef_chicharon_month = items_final_df.loc[items_final_df.loc[:,'items'] =='Exotic Extras Beef Chicharon']
beef_chicharon_month_count = beef_chicharon_month['quantity'].sum()

gummy_vitamins_month = items_final_df.loc[items_final_df.loc[:,'items'] =='HealthyKid 3+ Gummy Vitamins']
gummy_vitamins_month_count = gummy_vitamins_month['quantity'].sum()

yummy_vegetables_month = items_final_df.loc[items_final_df.loc[:,'items'] =='HealthyKid 3+ Yummy Vegetables']
yummy_vegetables_month_count = yummy_vegetables_month['quantity'].sum()

orange_beans_month = items_final_df.loc[items_final_df.loc[:,'items'] =='Candy City Orange Beans']
orange_beans_month_count = orange_beans_month['quantity'].sum()

nutritional_milk_month = items_final_df.loc[items_final_df.loc[:,'items'] =='HealthyKid 3+ Nutrional Milk']
nutritional_milk_month_count = nutritional_milk_month['quantity'].sum()

kimchi_seaweed_month = items_final_df.loc[items_final_df.loc[:,'items'] =='Exotic Extras Kimchi and Seaweed']
kimchi_seaweed_month_count = kimchi_seaweed_month['quantity'].sum()

gummy_worms_month = items_final_df.loc[items_final_df.loc[:,'items'] =='Candy City Gummy Worms']
gummy_worms_month_count = gummy_worms_month['quantity'].sum()


#####################################################################################################################################

def spliter(items): #creates a function to clean up unwanted strings
    items_list = items.replace(',',' ').split(';')
    return items_list

df_january['transaction_items'] = df_january['transaction_items'].apply(spliter) #apply function to df transac items

january_fixed_items = pd.DataFrame(df_january['transaction_items'].tolist()) #defines fixed_items as the list of new df
january_fixed_items.replace('',np.nan,regex=True,inplace=True) #replaces all blank values in the df
january_fixed_items_row = january_fixed_items.melt(value_name = 'january_items') #melts the df and renames value_name into 'month_items'
january_fixed_items_row.drop(columns=['variable'],inplace=True) #removes the column 'variable'
january_fixed_items_row.dropna(axis=0,how='all',inplace=True) #removes all missing values

def items_in_depth(n):
    fixed_items_final = []
    fixed_items_final.append(n[:n.find('(')-1])
    fixed_items_final.append(int(n[n.find(')')-1]))
    return fixed_items_final

january_fixed_items_row['as_list'] = january_fixed_items_row['january_items'].apply(items_in_depth)
january_items_final_df = pd.DataFrame(january_fixed_items_row['as_list'].tolist(), columns=['items','quantity'])

beef_chicharon_january = january_items_final_df.loc[january_items_final_df.loc[:,'items'] =='Exotic Extras Beef Chicharon']
beef_chicharon_january_count = beef_chicharon_january['quantity'].sum()

gummy_vitamins_january = january_items_final_df.loc[january_items_final_df.loc[:,'items'] =='HealthyKid 3+ Gummy Vitamins']
gummy_vitamins_january_count = gummy_vitamins_january['quantity'].sum()

yummy_vegetables_january = january_items_final_df.loc[january_items_final_df.loc[:,'items'] =='HealthyKid 3+ Yummy Vegetables']
yummy_vegetables_january_count = yummy_vegetables_january['quantity'].sum()

orange_beans_january = january_items_final_df.loc[january_items_final_df.loc[:,'items'] =='Candy City Orange Beans']
orange_beans_january_count = orange_beans_january['quantity'].sum()

nutritional_milk_january = january_items_final_df.loc[january_items_final_df.loc[:,'items'] =='HealthyKid 3+ Nutrional Milk']
nutritional_milk_january_count = nutritional_milk_january['quantity'].sum()

kimchi_seaweed_january = january_items_final_df.loc[january_items_final_df.loc[:,'items'] =='Exotic Extras Kimchi and Seaweed']
kimchi_seaweed_january_count = kimchi_seaweed_january['quantity'].sum()

gummy_worms_january = january_items_final_df.loc[january_items_final_df.loc[:,'items'] =='Candy City Gummy Worms']
gummy_worms_january_count = gummy_worms_january['quantity'].sum()


#####################################################################################################################################

def spliter(items): #creates a function to clean up unwanted strings
    items_list = items.replace(',',' ').split(';')
    return items_list

df_february['transaction_items'] = df_february['transaction_items'].apply(spliter) #apply function to df transac items

february_fixed_items = pd.DataFrame(df_february['transaction_items'].tolist()) #defines fixed_items as the list of new df
february_fixed_items.replace('',np.nan,regex=True,inplace=True) #replaces all blank values in the df
february_fixed_items_row = february_fixed_items.melt(value_name = 'february_items') #melts the df and renames value_name into 'month_items'
february_fixed_items_row.drop(columns=['variable'],inplace=True) #removes the column 'variable'
february_fixed_items_row.dropna(axis=0,how='all',inplace=True) #removes all missing values

def items_in_depth(n):
    fixed_items_final = []
    fixed_items_final.append(n[:n.find('(')-1])
    fixed_items_final.append(int(n[n.find(')')-1]))
    return fixed_items_final

february_fixed_items_row['as_list'] = february_fixed_items_row['february_items'].apply(items_in_depth)
february_items_final_df = pd.DataFrame(february_fixed_items_row['as_list'].tolist(), columns=['items','quantity'])

beef_chicharon_february = february_items_final_df.loc[february_items_final_df.loc[:,'items'] =='Exotic Extras Beef Chicharon']
beef_chicharon_february_count = beef_chicharon_february['quantity'].sum()

gummy_vitamins_february = february_items_final_df.loc[february_items_final_df.loc[:,'items'] =='HealthyKid 3+ Gummy Vitamins']
gummy_vitamins_february_count = gummy_vitamins_february['quantity'].sum()

yummy_vegetables_february = february_items_final_df.loc[february_items_final_df.loc[:,'items'] =='HealthyKid 3+ Yummy Vegetables']
yummy_vegetables_february_count = yummy_vegetables_february['quantity'].sum()

orange_beans_february = february_items_final_df.loc[february_items_final_df.loc[:,'items'] =='Candy City Orange Beans']
orange_beans_february_count = orange_beans_february['quantity'].sum()

nutritional_milk_february = february_items_final_df.loc[february_items_final_df.loc[:,'items'] =='HealthyKid 3+ Nutrional Milk']
nutritional_milk_february_count = nutritional_milk_february['quantity'].sum()

kimchi_seaweed_february = february_items_final_df.loc[february_items_final_df.loc[:,'items'] =='Exotic Extras Kimchi and Seaweed']
kimchi_seaweed_february_count = kimchi_seaweed_february['quantity'].sum()

gummy_worms_february = february_items_final_df.loc[february_items_final_df.loc[:,'items'] =='Candy City Gummy Worms']
gummy_worms_february_count = gummy_worms_february['quantity'].sum()


#####################################################################################################################################

def spliter(items): #creates a function to clean up unwanted strings
    items_list = items.replace(',',' ').split(';')
    return items_list

df_march['transaction_items'] = df_march['transaction_items'].apply(spliter) #apply function to df transac items

march_fixed_items = pd.DataFrame(df_march['transaction_items'].tolist()) #defines fixed_items as the list of new df
march_fixed_items.replace('',np.nan,regex=True,inplace=True) #replaces all blank values in the df
march_fixed_items_row = march_fixed_items.melt(value_name = 'march_items') #melts the df and renames value_name into 'month_items'
march_fixed_items_row.drop(columns=['variable'],inplace=True) #removes the column 'variable'
march_fixed_items_row.dropna(axis=0,how='all',inplace=True) #removes all missing values

def items_in_depth(n):
    fixed_items_final = []
    fixed_items_final.append(n[:n.find('(')-1])
    fixed_items_final.append(int(n[n.find(')')-1]))
    return fixed_items_final

march_fixed_items_row['as_list'] = march_fixed_items_row['march_items'].apply(items_in_depth)
march_items_final_df = pd.DataFrame(march_fixed_items_row['as_list'].tolist(), columns=['items','quantity'])

beef_chicharon_march = march_items_final_df.loc[march_items_final_df.loc[:,'items'] =='Exotic Extras Beef Chicharon']
beef_chicharon_march_count = beef_chicharon_march['quantity'].sum()

gummy_vitamins_march = march_items_final_df.loc[march_items_final_df.loc[:,'items'] =='HealthyKid 3+ Gummy Vitamins']
gummy_vitamins_march_count = gummy_vitamins_march['quantity'].sum()

yummy_vegetables_march = march_items_final_df.loc[march_items_final_df.loc[:,'items'] =='HealthyKid 3+ Yummy Vegetables']
yummy_vegetables_march_count = yummy_vegetables_march['quantity'].sum()

orange_beans_march = march_items_final_df.loc[march_items_final_df.loc[:,'items'] =='Candy City Orange Beans']
orange_beans_march_count = orange_beans_march['quantity'].sum()

nutritional_milk_march = march_items_final_df.loc[march_items_final_df.loc[:,'items'] =='HealthyKid 3+ Nutrional Milk']
nutritional_milk_march_count = nutritional_milk_march['quantity'].sum()

kimchi_seaweed_march = march_items_final_df.loc[march_items_final_df.loc[:,'items'] =='Exotic Extras Kimchi and Seaweed']
kimchi_seaweed_march_count = kimchi_seaweed_march['quantity'].sum()

gummy_worms_march = march_items_final_df.loc[march_items_final_df.loc[:,'items'] =='Candy City Gummy Worms']
gummy_worms_march_count = gummy_worms_march['quantity'].sum()


#####################################################################################################################################

def spliter(items): #creates a function to clean up unwanted strings
    items_list = items.replace(',',' ').split(';')
    return items_list

df_april['transaction_items'] = df_april['transaction_items'].apply(spliter) #apply function to df transac items

april_fixed_items = pd.DataFrame(df_april['transaction_items'].tolist()) #defines fixed_items as the list of new df
april_fixed_items.replace('',np.nan,regex=True,inplace=True) #replaces all blank values in the df
april_fixed_items_row = april_fixed_items.melt(value_name = 'april_items') #melts the df and renames value_name into 'month_items'
april_fixed_items_row.drop(columns=['variable'],inplace=True) #removes the column 'variable'
april_fixed_items_row.dropna(axis=0,how='all',inplace=True) #removes all missing values

def items_in_depth(n):
    fixed_items_final = []
    fixed_items_final.append(n[:n.find('(')-1])
    fixed_items_final.append(int(n[n.find(')')-1]))
    return fixed_items_final

april_fixed_items_row['as_list'] = april_fixed_items_row['april_items'].apply(items_in_depth)
april_items_final_df = pd.DataFrame(april_fixed_items_row['as_list'].tolist(), columns=['items','quantity'])

beef_chicharon_april = april_items_final_df.loc[april_items_final_df.loc[:,'items'] =='Exotic Extras Beef Chicharon']
beef_chicharon_april_count = beef_chicharon_april['quantity'].sum()

gummy_vitamins_april = april_items_final_df.loc[april_items_final_df.loc[:,'items'] =='HealthyKid 3+ Gummy Vitamins']
gummy_vitamins_april_count = gummy_vitamins_april['quantity'].sum()

yummy_vegetables_april = april_items_final_df.loc[april_items_final_df.loc[:,'items'] =='HealthyKid 3+ Yummy Vegetables']
yummy_vegetables_april_count = yummy_vegetables_april['quantity'].sum()

orange_beans_april = april_items_final_df.loc[april_items_final_df.loc[:,'items'] =='Candy City Orange Beans']
orange_beans_april_count = orange_beans_april['quantity'].sum()

nutritional_milk_april = april_items_final_df.loc[april_items_final_df.loc[:,'items'] =='HealthyKid 3+ Nutrional Milk']
nutritional_milk_april_count = nutritional_milk_april['quantity'].sum()

kimchi_seaweed_april = april_items_final_df.loc[april_items_final_df.loc[:,'items'] =='Exotic Extras Kimchi and Seaweed']
kimchi_seaweed_april_count = kimchi_seaweed_april['quantity'].sum()

gummy_worms_april = april_items_final_df.loc[april_items_final_df.loc[:,'items'] =='Candy City Gummy Worms']
gummy_worms_april_count = gummy_worms_april['quantity'].sum()


#####################################################################################################################################

def spliter(items): #creates a function to clean up unwanted strings
    items_list = items.replace(',',' ').split(';')
    return items_list

df_may['transaction_items'] = df_may['transaction_items'].apply(spliter) #apply function to df transac items

may_fixed_items = pd.DataFrame(df_may['transaction_items'].tolist()) #defines fixed_items as the list of new df
may_fixed_items.replace('',np.nan,regex=True,inplace=True) #replaces all blank values in the df
may_fixed_items_row = may_fixed_items.melt(value_name = 'may_items') #melts the df and renames value_name into 'month_items'
may_fixed_items_row.drop(columns=['variable'],inplace=True) #removes the column 'variable'
may_fixed_items_row.dropna(axis=0,how='all',inplace=True) #removes all missing values

def items_in_depth(n):
    fixed_items_final = []
    fixed_items_final.append(n[:n.find('(')-1])
    fixed_items_final.append(int(n[n.find(')')-1]))
    return fixed_items_final

may_fixed_items_row['as_list'] = may_fixed_items_row['may_items'].apply(items_in_depth)
may_items_final_df = pd.DataFrame(may_fixed_items_row['as_list'].tolist(), columns=['items','quantity'])

beef_chicharon_may = may_items_final_df.loc[may_items_final_df.loc[:,'items'] =='Exotic Extras Beef Chicharon']
beef_chicharon_may_count = beef_chicharon_may['quantity'].sum()

gummy_vitamins_may = may_items_final_df.loc[may_items_final_df.loc[:,'items'] =='HealthyKid 3+ Gummy Vitamins']
gummy_vitamins_may_count = gummy_vitamins_may['quantity'].sum()

yummy_vegetables_may = may_items_final_df.loc[may_items_final_df.loc[:,'items'] =='HealthyKid 3+ Yummy Vegetables']
yummy_vegetables_may_count = yummy_vegetables_may['quantity'].sum()

orange_beans_may = may_items_final_df.loc[may_items_final_df.loc[:,'items'] =='Candy City Orange Beans']
orange_beans_may_count = orange_beans_may['quantity'].sum()

nutritional_milk_may = may_items_final_df.loc[may_items_final_df.loc[:,'items'] =='HealthyKid 3+ Nutrional Milk']
nutritional_milk_may_count = nutritional_milk_may['quantity'].sum()

kimchi_seaweed_may = may_items_final_df.loc[may_items_final_df.loc[:,'items'] =='Exotic Extras Kimchi and Seaweed']
kimchi_seaweed_may_count = kimchi_seaweed_may['quantity'].sum()

gummy_worms_may = may_items_final_df.loc[may_items_final_df.loc[:,'items'] =='Candy City Gummy Worms']
gummy_worms_may_count = gummy_worms_may['quantity'].sum()


#####################################################################################################################################

def spliter(items): #creates a function to clean up unwanted strings
    items_list = items.replace(',',' ').split(';')
    return items_list

df_june['transaction_items'] = df_june['transaction_items'].apply(spliter) #apply function to df transac items

june_fixed_items = pd.DataFrame(df_june['transaction_items'].tolist()) #defines fixed_items as the list of new df
june_fixed_items.replace('',np.nan,regex=True,inplace=True) #replaces all blank values in the df
june_fixed_items_row = june_fixed_items.melt(value_name = 'june_items') #melts the df and renames value_name into 'month_items'
june_fixed_items_row.drop(columns=['variable'],inplace=True) #removes the column 'variable'
june_fixed_items_row.dropna(axis=0,how='all',inplace=True) #removes all missing values

def items_in_depth(n):
    fixed_items_final = []
    fixed_items_final.append(n[:n.find('(')-1])
    fixed_items_final.append(int(n[n.find(')')-1]))
    return fixed_items_final

june_fixed_items_row['as_list'] = june_fixed_items_row['june_items'].apply(items_in_depth)
june_items_final_df = pd.DataFrame(june_fixed_items_row['as_list'].tolist(), columns=['items','quantity'])

beef_chicharon_june = june_items_final_df.loc[june_items_final_df.loc[:,'items'] =='Exotic Extras Beef Chicharon']
beef_chicharon_june_count = beef_chicharon_june['quantity'].sum()

gummy_vitamins_june = june_items_final_df.loc[june_items_final_df.loc[:,'items'] =='HealthyKid 3+ Gummy Vitamins']
gummy_vitamins_june_count = gummy_vitamins_june['quantity'].sum()

yummy_vegetables_june = june_items_final_df.loc[june_items_final_df.loc[:,'items'] =='HealthyKid 3+ Yummy Vegetables']
yummy_vegetables_june_count = yummy_vegetables_june['quantity'].sum()

orange_beans_june = june_items_final_df.loc[june_items_final_df.loc[:,'items'] =='Candy City Orange Beans']
orange_beans_june_count = orange_beans_june['quantity'].sum()

nutritional_milk_june = june_items_final_df.loc[june_items_final_df.loc[:,'items'] =='HealthyKid 3+ Nutrional Milk']
nutritional_milk_june_count = nutritional_milk_june['quantity'].sum()

kimchi_seaweed_june = june_items_final_df.loc[june_items_final_df.loc[:,'items'] =='Exotic Extras Kimchi and Seaweed']
kimchi_seaweed_june_count = kimchi_seaweed_june['quantity'].sum()

gummy_worms_june = june_items_final_df.loc[june_items_final_df.loc[:,'items'] =='Candy City Gummy Worms']
gummy_worms_june_count = gummy_worms_june['quantity'].sum()

#####################################################################################################################################

breakdown_quantity = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'Total'], 'Beef Chicharon': [beef_chicharon_january_count, beef_chicharon_february_count, beef_chicharon_march_count, beef_chicharon_april_count, beef_chicharon_may_count, beef_chicharon_june_count, beef_chicharon_month_count]}
breakdown_quantity_df = pd.DataFrame(breakdown_quantity)
breakdown_quantity_df.insert(2, 'Gummy Vitamins', [gummy_vitamins_january_count, gummy_vitamins_february_count, gummy_vitamins_march_count, gummy_vitamins_april_count, gummy_vitamins_may_count, gummy_vitamins_june_count, gummy_vitamins_month_count], True)
breakdown_quantity_df.insert(3, 'Yummy Vegetables', [yummy_vegetables_january_count, yummy_vegetables_february_count, yummy_vegetables_march_count, yummy_vegetables_april_count, yummy_vegetables_may_count, yummy_vegetables_june_count, yummy_vegetables_month_count], True)
breakdown_quantity_df.insert(4, 'Orange Beans', [orange_beans_january_count, orange_beans_february_count, orange_beans_march_count, orange_beans_april_count, orange_beans_may_count, orange_beans_june_count, orange_beans_month_count], True)
breakdown_quantity_df.insert(5, 'Nutritional Milk', [nutritional_milk_january_count, nutritional_milk_february_count, nutritional_milk_march_count, nutritional_milk_april_count, nutritional_milk_may_count, nutritional_milk_june_count, nutritional_milk_month_count], True)
breakdown_quantity_df.insert(6, 'Kimchi & Seaweed', [kimchi_seaweed_january_count, kimchi_seaweed_february_count, kimchi_seaweed_march_count, kimchi_seaweed_april_count, kimchi_seaweed_may_count, kimchi_seaweed_june_count, kimchi_seaweed_month_count], True)
breakdown_quantity_df.insert(7, 'Gummy Worms', [gummy_worms_january_count, gummy_worms_february_count, gummy_worms_march_count, gummy_worms_april_count, gummy_worms_may_count, gummy_worms_june_count, gummy_worms_month_count], True)

#####################################################################################################################################

beef_chicharon_price = 1299
gummy_vitamins_price = 1500
yummy_vegetables_price = 500
orange_beans_price = 199
nutritional_milk_price = 1990
kimchi_seaweed_price = 799
gummy_worms_price = 150

beef_chicharon_january_sales = beef_chicharon_january_count * beef_chicharon_price
beef_chicharon_february_sales = beef_chicharon_february_count * beef_chicharon_price
beef_chicharon_march_sales = beef_chicharon_march_count * beef_chicharon_price
beef_chicharon_april_sales = beef_chicharon_april_count * beef_chicharon_price
beef_chicharon_may_sales = beef_chicharon_may_count * beef_chicharon_price
beef_chicharon_june_sales = beef_chicharon_june_count * beef_chicharon_price
beef_chicharon_month_sales = beef_chicharon_month_count * beef_chicharon_price

gummy_vitamins_january_sales = gummy_vitamins_january_count * gummy_vitamins_price
gummy_vitamins_february_sales = gummy_vitamins_february_count * gummy_vitamins_price
gummy_vitamins_march_sales = gummy_vitamins_march_count * gummy_vitamins_price
gummy_vitamins_april_sales = gummy_vitamins_april_count * gummy_vitamins_price
gummy_vitamins_may_sales = gummy_vitamins_may_count * gummy_vitamins_price
gummy_vitamins_june_sales = gummy_vitamins_june_count * gummy_vitamins_price
gummy_vitamins_month_sales = gummy_vitamins_month_count * gummy_vitamins_price

yummy_vegetables_january_sales = yummy_vegetables_january_count * yummy_vegetables_price
yummy_vegetables_february_sales = yummy_vegetables_february_count * yummy_vegetables_price
yummy_vegetables_march_sales = yummy_vegetables_march_count * yummy_vegetables_price
yummy_vegetables_april_sales = yummy_vegetables_april_count * yummy_vegetables_price
yummy_vegetables_may_sales = yummy_vegetables_may_count * yummy_vegetables_price
yummy_vegetables_june_sales = yummy_vegetables_june_count * yummy_vegetables_price
yummy_vegetables_month_sales = yummy_vegetables_month_count * yummy_vegetables_price

orange_beans_january_sales = orange_beans_january_count * orange_beans_price
orange_beans_february_sales = orange_beans_february_count * orange_beans_price
orange_beans_march_sales = orange_beans_march_count * orange_beans_price
orange_beans_april_sales = orange_beans_april_count * orange_beans_price
orange_beans_may_sales = orange_beans_may_count * orange_beans_price
orange_beans_june_sales = orange_beans_june_count * orange_beans_price
orange_beans_month_sales = orange_beans_month_count * orange_beans_price

nutritional_milk_january_sales = nutritional_milk_january_count * nutritional_milk_price
nutritional_milk_february_sales = nutritional_milk_february_count * nutritional_milk_price
nutritional_milk_march_sales = nutritional_milk_march_count * nutritional_milk_price
nutritional_milk_april_sales = nutritional_milk_april_count * nutritional_milk_price
nutritional_milk_may_sales = nutritional_milk_may_count * nutritional_milk_price
nutritional_milk_june_sales = nutritional_milk_june_count * nutritional_milk_price
nutritional_milk_month_sales = nutritional_milk_month_count * nutritional_milk_price

kimchi_seaweed_january_sales = kimchi_seaweed_january_count * kimchi_seaweed_price
kimchi_seaweed_february_sales = kimchi_seaweed_february_count * kimchi_seaweed_price
kimchi_seaweed_march_sales = kimchi_seaweed_march_count * kimchi_seaweed_price
kimchi_seaweed_april_sales = kimchi_seaweed_april_count * kimchi_seaweed_price
kimchi_seaweed_may_sales = kimchi_seaweed_may_count * kimchi_seaweed_price
kimchi_seaweed_june_sales = kimchi_seaweed_june_count * kimchi_seaweed_price
kimchi_seaweed_month_sales = kimchi_seaweed_month_count * kimchi_seaweed_price

gummy_worms_january_sales = gummy_worms_january_count * gummy_worms_price
gummy_worms_february_sales = gummy_worms_february_count * gummy_worms_price
gummy_worms_march_sales = gummy_worms_march_count * gummy_worms_price
gummy_worms_april_sales = gummy_worms_april_count * gummy_worms_price
gummy_worms_may_sales = gummy_worms_may_count * gummy_worms_price
gummy_worms_june_sales = gummy_worms_june_count * gummy_worms_price
gummy_worms_month_sales = gummy_worms_month_count * gummy_worms_price

sales_quantity = {'Month': ['January', 'February', 'March', 'April', 'May', 'June', 'Total'], 'Beef Chicharon': [beef_chicharon_january_sales, beef_chicharon_february_sales, beef_chicharon_march_sales, beef_chicharon_april_sales, beef_chicharon_may_sales, beef_chicharon_june_sales, beef_chicharon_month_sales]}
sales_quantity_df = pd.DataFrame(sales_quantity)
sales_quantity_df.insert(2, 'Gummy Vitamins', [gummy_vitamins_january_sales, gummy_vitamins_february_sales, gummy_vitamins_march_sales, gummy_vitamins_april_sales, gummy_vitamins_may_sales, gummy_vitamins_june_sales, gummy_vitamins_month_sales], True)
sales_quantity_df.insert(3, 'Yummy Vegetables', [yummy_vegetables_january_sales, yummy_vegetables_february_sales, yummy_vegetables_march_sales, yummy_vegetables_april_sales, yummy_vegetables_may_sales, yummy_vegetables_june_sales, yummy_vegetables_month_sales], True)
sales_quantity_df.insert(4, 'Orange Beans', [orange_beans_january_sales, orange_beans_february_sales, orange_beans_march_sales, orange_beans_april_sales, orange_beans_may_sales, orange_beans_june_sales, orange_beans_month_sales], True)
sales_quantity_df.insert(5, 'Nutritional Milk', [nutritional_milk_january_sales, nutritional_milk_february_sales, nutritional_milk_march_sales, nutritional_milk_april_sales, nutritional_milk_may_sales, nutritional_milk_june_sales, nutritional_milk_month_sales], True)
sales_quantity_df.insert(6, 'Kimchi & Seaweed', [kimchi_seaweed_january_sales, kimchi_seaweed_february_sales, kimchi_seaweed_march_sales, kimchi_seaweed_april_sales, kimchi_seaweed_may_sales, kimchi_seaweed_june_sales, kimchi_seaweed_month_sales], True)
sales_quantity_df.insert(7, 'Gummy Worms', [gummy_worms_january_sales, gummy_worms_february_sales, gummy_worms_march_sales, gummy_worms_april_sales, gummy_worms_may_sales, gummy_worms_june_sales, gummy_worms_month_sales], True)

#####################################################################################################################################

january_customers = list(df_january['name'].unique())
february_customers = list(df_february['name'].unique())
march_customers = list(df_march['name'].unique())
april_customers = list(df_april['name'].unique())
may_customers = list(df_may['name'].unique())
june_customers = list(df_june['name'].unique())

january_repeaters = 0
february_repeaters = sum(n in january_customers for n in february_customers)
march_repeaters = sum(n in february_customers for n in march_customers)
april_repeaters = sum(n in march_customers for n in april_customers)
may_repeaters = sum(n in april_customers for n in may_customers)
june_repeaters = sum(n in may_customers for n in june_customers)

customer_data = {'January': [], 'February': [], 'March': [], 'April': [], 'May': [], 'June': []}
customer_df = pd.DataFrame(customer_data)
customer_df.loc['Repeaters'] = [january_repeaters, february_repeaters, march_repeaters, april_repeaters, may_repeaters, june_repeaters]

#####################################################################################################################################

january_to_february = list(np.unique(january_customers + february_customers)) # gets the unique values in the lists stated
january_to_march = list(np.unique(january_customers + february_customers + march_customers))
january_to_april = list(np.unique(january_customers + february_customers + march_customers + april_customers))
january_to_may = list(np.unique(january_customers + february_customers + march_customers + april_customers + may_customers))

january_inactive = 0
february_inactive = len(list(set(january_customers) - set(february_customers))) # gets the value of customers who are in the first list but not in the second
march_inactive = len(list(set(january_to_february) - set(march_customers))) # // gets the customers who have activity in previous months but not the current
april_inactive = len(list(set(january_to_march) - set(april_customers)))
may_inactive = len(list(set(january_to_april) - set(may_customers)))
june_inactive = len(list(set(january_to_may) - set(june_customers)))
customer_df.loc['Inactive'] = [january_inactive, february_inactive, march_inactive, april_inactive, may_inactive, june_inactive]

#####################################################################################################################################

rolling_january = january_customers
rolling_february = january_customers
rolling_march = list(set.intersection(*map(set, [january_customers, february_customers])))
rolling_april = list(set.intersection(*map(set, [january_customers, february_customers, march_customers])))
rolling_may = list(set.intersection(*map(set, [january_customers, february_customers, march_customers, april_customers])))
rolling_june = list(set.intersection(*map(set, [january_customers, february_customers, march_customers, april_customers, may_customers])))

january_engaged = len(january_customers)
february_engaged = sum(n in rolling_february for n in february_customers)
march_engaged = sum(n in rolling_march for n in march_customers)
april_engaged = sum(n in rolling_april for n in april_customers)
may_engaged = sum(n in rolling_may for n in may_customers)
june_engaged = sum(n in rolling_june for n in june_customers)
customer_df.loc['Engaged'] = [january_engaged, february_engaged, march_engaged, april_engaged, may_engaged, june_engaged]

#####################################################################################################################################

# IMPORTANT VARIABLES : breakdown_quantity_df, sales_quantity_df, customer_df

months = ['January', 'February', 'March', 'April', 'May', 'June']
beef_chicharon_summary = [beef_chicharon_january_count, beef_chicharon_february_count, beef_chicharon_march_count, beef_chicharon_april_count, beef_chicharon_may_count, beef_chicharon_june_count]
gummy_vitamins_summary = [gummy_vitamins_january_count, gummy_vitamins_february_count, gummy_vitamins_march_count, gummy_vitamins_april_count, gummy_vitamins_may_count, gummy_vitamins_june_count]
yummy_vegetables_summary = [yummy_vegetables_january_count, yummy_vegetables_february_count, yummy_vegetables_march_count, yummy_vegetables_april_count, yummy_vegetables_may_count, yummy_vegetables_june_count]
orange_beans_summary = [orange_beans_january_count, orange_beans_february_count, orange_beans_march_count, orange_beans_april_count, orange_beans_may_count, orange_beans_june_count]
nutritional_milk_summary = [nutritional_milk_january_count, nutritional_milk_february_count, nutritional_milk_march_count, nutritional_milk_april_count, nutritional_milk_may_count, nutritional_milk_june_count]
kimchi_seaweed_summary = [kimchi_seaweed_january_count, kimchi_seaweed_february_count, kimchi_seaweed_march_count, kimchi_seaweed_april_count, kimchi_seaweed_may_count, kimchi_seaweed_june_count]
gummy_worms_summary = [gummy_worms_january_count, gummy_worms_february_count, gummy_worms_march_count, gummy_worms_april_count, gummy_worms_may_count, gummy_worms_june_count]

repeaters_summary = [january_repeaters, february_repeaters, march_repeaters, april_repeaters, may_repeaters, june_repeaters]
inactive_summary = [january_inactive, february_inactive, march_inactive, april_inactive, may_inactive, june_inactive]
engaged_summary = [january_engaged, february_engaged, march_engaged, april_engaged, may_engaged, june_engaged]

def linegraph(x, y, title):
    plt.plot(x, y, color='red', marker='o')
    plt.title(title, fontsize=14)
    plt.grid(True)
    return plt.figure()

beef_chicharon_graph = linegraph(months, beef_chicharon_summary, 'Beef Chicharon Summary')
gummy_vitamins_graph = linegraph(months, gummy_vitamins_summary, 'Gummy Vitamins Summary')
yummy_vegetables_graph = linegraph(months, yummy_vegetables_summary, 'Yummy Vegetables Summary')
orange_beans_graph = linegraph(months, orange_beans_summary, 'Orange Beans Summary')
nutritional_milk_graph = linegraph(months, nutritional_milk_summary, 'Nutritional Milk Summary')
kimchi_seaweed_graph = linegraph(months, kimchi_seaweed_summary, 'Kimchi & Seaweed Summary')
gummy_worms_graph = linegraph(months, gummy_worms_summary, 'Gummy Worms Summary')
repeaters_graph = linegraph(months, repeaters_summary, 'Repeaters Summary')
inactive_graph = linegraph(months, inactive_summary, 'Inactive Summary')
engaged_graph = linegraph(months, engaged_summary, 'Engaged Summary')

# RAW DATAFRAMES FOR THE QUESTIONS : breakdown_quantity_df, sales_quantity_df, customer_df