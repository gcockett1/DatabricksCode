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


