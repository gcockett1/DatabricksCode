# Databricks notebook source
import pandas as pd

# COMMAND ----------

df = pd.DataFrame({
    'a' : [1,2,3],
    'b' : [4,5,6], 
    'c' : [7,8,9], 
}, index = [1,2,3])


df2 = pd.DataFrame(
    [[1,2,3],[4,5,6],[7,8,9]],
    index =[1,2,3],
    columns = ['a', 'b', 'c'])

print(df)
print("break")
print(df2)



# COMMAND ----------

df.loc[1,'c']
df.iloc[0,2]

df.loc[2,['b','c']]
df.iloc[1,1:3]

df.loc[:,'a']
df.iloc[:,0]

# COMMAND ----------

pd.concat([df,df], axis=1)
pd.concat([df,df])

# COMMAND ----------

df.sort_values('a', ascending=False)
df.sort_values(1, axis=1, ascending=False)

# COMMAND ----------

df.drop(columns='c')
df.drop([1,3])

# COMMAND ----------

tipsData = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

#print(tipsData)

print(tipsData.head(5))
print(tipsData.describe())
print(tipsData.isnull().sum())

# COMMAND ----------

tipsData.groupby(['day']).count()

# COMMAND ----------

tipsData.groupby(['day']).sum()

# COMMAND ----------

totalTips = tipsData.groupby(['day']).sum()['tip']
totalBill = tipsData.groupby(['day']).sum()['total_bill']

tipdaypercentage = (100 * totalTips/totalBill)

tipdaypercentage = tipdaypercentage.to_frame('tip(%)').reset_index()

print(tipdaypercentage)

# COMMAND ----------

pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

# COMMAND ----------

pd.DataFrame({'Bob': ['I liked it.', 'It was awful.', 'wadiya'], 
              'Sue': ['Pretty good.', 'Bland.', 'talkinabeet']},
             index = ['product a', 'product b', 'product c'], )



# COMMAND ----------

pd.Series([1, 2, 3, 4, 5])


# COMMAND ----------

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')

# COMMAND ----------

animals = pd.DataFrame({'Cows': [12, 20], 'Goats': [22, 19]}, index=['Year 1', 'Year 2'])

animals.to_csv("cows_and_goats.csv")

# COMMAND ----------

reviews = pd.read_csv("../input/wine-reviews/winemag-data_first150k.csv", index_col=0)

# COMMAND ----------

ingredients = pd.Series(['4 cups', '1 cup', '2 large', '1 can'], 
            index=['Flour', 'Milk', 'Eggs', 'Spam'], 
            name='Dinner')
print(ingredients)

# COMMAND ----------

import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
pd.set_option("display.max_rows", 5)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.indexing_selecting_and_assigning import *
print("Setup complete.")

# COMMAND ----------

top_oceania_wines = reviews.loc[
    (reviews.country.isin(['Australia', 'New Zealand']))
    & (reviews.points >= 95)
]

# COMMAND ----------

italian_wines = reviews.loc[reviews.country == 'Italy']

# COMMAND ----------

cols = ['country', 'variety']
df = reviews.loc[:99, cols]
or

cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]\


# COMMAND ----------


cols = ['country', 'variety']
df = reviews.loc[:99, cols]


cols_idx = [0, 11]
df = reviews.iloc[:100, cols_idx]

# COMMAND ----------

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

# COMMAND ----------

indices = [1, 2, 3, 5, 8]
sample_reviews = reviews.loc[indices]

# COMMAND ----------

first_descriptions = reviews.description.iloc[:10]

# COMMAND ----------

first_row = reviews.iloc[0]

# COMMAND ----------

first_description = reviews.description.iloc[0]

# COMMAND ----------

desc = reviews.description

# COMMAND ----------


