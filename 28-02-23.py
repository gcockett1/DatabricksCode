# Databricks notebook source
import numpy as np
import pyspark as py
import matplotlib.pyplot as plt

dataRaw = spark.read.csv(path = "dbfs:/FileStore/IrisData/iris_head_num.txt")
dataRaw = np.array(dataRaw.select("*").collect())
header = dataRaw[0,:]
data = dataRaw[1:, :4]
data = np.vstack(data.astype(np.float32))

labels = np.vstack(dataRaw[1:, :4].astype(np.float32))

labelsUn, labelscounts = np.unique(labels, return_counts = 1)

# COMMAND ----------

nrows,ncols = np.shape(data)
nclasses = len(labelsUn)
average = np.zeros((nclasses,ncols))
maxi = np.zeros((nclasses,ncols))
sd = np.zeros((nclasses,ncols))
for i in labelsUn:
    indexes = np.reshape(labels==i, nrows)
    average[i-1,:] = np.mean(data[indexes,:],axis=0)
    maxi[i-1,:] = np.max(data[indexes,:],axis=0)
    mini[i-1,:] = np.min(data[indexes,:],axis=0)
    sd[i-1,:] = np.std(data[indexes,:],axis=0)

# COMMAND ----------

species = np.array(['setosa', 'versicolour', 'virginica'])
features = np.array(header[:-1].astype("U"))
x = np.arange(len(features))

fig,ax = plt.subplots()
for i in labelsUn:
    ax.errorbar(x, average[i-1,:], sd[i-1,:], marker = "o", label=species[i-1,:])
    
ax.legend(loc="upper right")
ax.set_xlabel("features", fontsize = 14, fontweight = 'bold')
ax.set_ylabel("mean +/- sd", fontsize = 14, fontweight = 'bold')
ax.set_xticks(x)
ax.set_xticklabels(features, rotation=45)

fig.tight_layout()



# COMMAND ----------

outliers = dict(marker='+', markerfacecolor='black')
medians = dict(linewidth=2)
boxes = np.array([dict(facecolor='r', color='r'), 
                  dict(facecolor='g', color='g'),
                  dict(facecolor='b', color='b')])

mylegend = [plt.scatter([0],[0], facecolor='r', edgecolor='r', label=species[0]), 
            plt.scatter([0],[0], facecolor='g', edgecolor='g', label=species[1]),
            plt.scatter([0],[0], facecolor='b', edgecolor='b', label=species[2])]

plt.close("all")

# COMMAND ----------

x = -7
step = 5
fig, ax = plt.subplots

for j in range(len(features)):
    x+=7
    for i in labelsUn:
        indexes = np.reshape(labels==i,nrows)
        temp = data[indexes,j]
        ax.boxplot(temp, positions=[x], 
                  widths=2, 
                  patch_artist = True
                  medianprops=medians, 
                  boxprops=boxes[i-1], 
                  flierprops=outliers)
        x+=step

ax.set_title("iris data set", fontsize=13, fontweight = 'bold')
ax.set_ylabel("values", fontsize = 14, fontweight = 'bold')
ax.set_xticks(np.arange(step,x,22))
ax.set_xticklabels(features, fontweight = 'bold', rotation=45)
ax.legend(handles=mylegend)
fig.tight_layout()
        

# COMMAND ----------

  import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("D:\\Python\\Articles\\matplotlib\\sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt  

df = pd.read_csv("D:\\Python\\Articles\\matplotlib\\company_sales_data.csv")
profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()

plt.plot(monthList, profitList, label = 'Profit data of last year', 
      color='r', marker='o', markerfacecolor='k', 
      linestyle='--', linewidth=3)
      
plt.xlabel('Month Number')
plt.ylabel('Profit in dollar')
plt.legend(loc='lower right')
plt.title('Company Sales data of last year')
plt.xticks(monthList)
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()

# COMMAND ----------


