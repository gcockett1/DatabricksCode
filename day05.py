# Databricks notebook source
import numpy as np

# COMMAND ----------

my1dArray = np.array([1,2,3])
my2dArray = np.array([1,2,3], [4,5,6])
my2dArray = np.array(((1,2,3), (4,5,6)), dtype = np.float32)

charArray1 = np.array([(1, 'a', 3.), (4,5, 'zzz')], dtype = 'U21')

print(charArray1)

# COMMAND ----------

rows = 4
cols = 3

array1s = np.ones((rows, cols))

array5s = 5 * np.ones((rows, cols))

array7s = np.full((rows, cols), 7)

print(array5s)
print(array7s)

# COMMAND ----------

samples = 5
step = 3
start = 10
stop = 24

np.arange(start, stop, step)
np.linspace(start, stop, samples)
np.eye(3)

np.random.random(2,3)


np.random.randint(0,10, (3,3))

# COMMAND ----------

a = np.array([[1,2,3], [4,5,6], [7,8,9]])

a.ndim
a.shape
a.size
a.dtype

a[a<9]
np.diag(a)

# COMMAND ----------

a = np.array([[1,2], [4,5]])
b = np.array([[9,8], [6,5]])


a + b

a - b

a * b

a / b

np.exp(a)

np.sqrt(a)

np.sin(a)
np.cos(a)
np.log(a)

display(a.dot(b))


# COMMAND ----------

# DBTITLE 1,pythagoras stuff, calculate length of hypotenuse using numpy :-/
from numpy import linalg as la

A = (0,0)
B = (0,3)
C = (1.5,0)

AB2 = la.norm(A-B)

AC2 = la.norm(A-C)

BC2 = la.norm(B-C)

print(BC2, BC)



# COMMAND ----------

import numpy as np

dataRaw = spark.read.csv(path = "dbfs:/FileStore/IrisData/iris_head_num.txt")

dataRaw = np.array(dataRaw.select("*").collect())

header = dataRaw[0,:]

data = dataRaw[1:, :4]

data = np.vstack(data.astype(np.float32))

labels = np.vstack(dataRaw[1:, 4].astype(np.int32))

labelsUn, labelsCounts = np.unique(labels, return_counts = 1)

display(labelsUn, labelsCounts)

# COMMAND ----------

nrows,ncols = np.shape(data)

nclasses = len(labelsUn)

average = np.zeros((nclasses, ncols))
maxi = np.zeros((nclasses, ncols))
mini = np.zeros((nclasses, ncols))
sd = np.zeros((nclasses, ncols))

for i in labelsUn:
    indexes = np.reshape(labels==i,nrows)
    average[i-1,:] = np.mean(data[indexes,:],axis=0)
    maxi[i-1,:] = np.max(data[indexes,:],axis=0)
    mini[i-1,:] = np.min(data[indexes,:],axis=0)
    sd[i-1,:] = np.std(data[indexes,:],axis=0)
print(header)
print("averages")
print(average)
print("maximum")
print(maxi)
print("minimum")
print(mini)
print("standard deviation")
print(sd)

# COMMAND ----------

outliers2sd = np.zeros((nclasses, ncols))
for i in labelsUn:
    indexes = np.reshape(labels==i, nrows)
    classData = data[indexes,:]
    for j in range(ncols):
        thresholdlow = average[i-1,j]-2*sd[i-1,j]
        thresholdhigh = average[i-1,j]+2*sd[i-1,j]
        remain = [x for x in classData[:,j] if(x > thresholdlow)]
        remain = [x for x in classData[:,j] if(x < thresholdhigh)]
        
        outliers2sd[i-1,j] = 100 * (labelsCounts[i-1] - len(remain)) / labelsCounts[i-1]

print(header)
print(outliers2sd)

# COMMAND ----------

decimals = 2
fmt = "%.2f"
formatf = ".csv"
import pandas as pd

species = np.array(['setosa', 'versicolour', 'virginica'])
for i in range(len(labelsUn)):
    
    temp = np.vstack( [average[i,:], mini[i,:], maxi[i,:], sd[i,:], outliers2sd[i,:]] ).T
    
    temp = np.around(temp,decimals)
    
    temp_str = np.char.mod(fmt, temp)
    
    rows = np.array(header[:-1].astype("U"))[:, np.newaxis]
    
    rowsf = np.hstack((rows, temp_str))
    
    headerf = [species[i], 'mean', 'min', 'max', 'sd', 'outliers2sd%']
    
    pdDf = pd.DataFrame(rowsf, columns = [headerf])
    
print(pdDf)

try:
    sparkDf.coalesce(1).write.format("com.databricks.spark.csv").option("header", "true").save("dbfs:/FileStore/tables/irisTest/" + str(species[i]))
    
except:
    print("file already exists")
    
display(spark.read.csv("dbfs:/FileStore/tables/irisTest/" + str(species[i])))

# COMMAND ----------

# DBTITLE 1,line graph, be sure to import matplotlib.pyplot and numpy
import matplotlib.pyplot as plt
import numpy as np

y = np.linspace(-1,1,5)
x = np.arange(5)

fig = plt.figure()
ax = fig.subplots()

line1 = ax.plot(x,y)

# COMMAND ----------

# DBTITLE 1,6 line plots 
y = np.linspace(-1,1,5)
x = np.arange(5)

number_rows = 3
number_cols = 2
fig2 = plt.figure()
ax2 = fig2.subplots(number_rows,number_cols)
ax2[0,1].plot(x,y)

# COMMAND ----------

# DBTITLE 1,Basic line plot
y = np.linspace(-1,1,5)
x = np.arange(5)

fig = plt.figure()
ax = fig.subplots()

y2 = np.linspace(-2,2,5) #new x and y statements can create new lines

line1 = ax.plot(x,y)
line2 = ax.plot(x,y2) #using x and y2, need to define both coordinates before issuing the statements

# COMMAND ----------

# DBTITLE 1,4 different charts
y1 = np.arange(0,110,10)
y2 = np.random.random(11)
x = np.arange(11)

fig, ax = plt.subplots(2,2)
ax[0,0].plot(x,y1)
ax[0,1].scatter(x,y2)
ax[1,0].bar(x,y1)
ax[1,1].barh(x,y1)

# COMMAND ----------

# DBTITLE 1,Trig graphs in python. ;-)
x = np.arange(0, 4*np.pi, 0.05) # every 0.05 interval in x is calculated, creates a better curve with smaller intervals
ycos = np.cos(x)
ysin = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, ycos, 'b-', label="cos(x)") # b = blue, - = bold line
ax.plot(x, ysin, 'r--', label="sin(x)") # r = red, -- = dotted line

ax.set_title("Trigonometric Functions")
ax.set_xlabel("0 to 4pi")
ax.set_ylabel("cos(x) and sin(x)")
ax.legend()

fig.tight_layout()

# COMMAND ----------

fig, ax = plt.subplots(1,2)

fig.suptitle("Horizontal and Vertical lines", fontsize = 14)

ax[0].set_title('Horizontal lines', fontstyle = 'italic')
ax[1].set_title('Vertical lines', fontname = 'Arial', fontstyle = 'italic')

ax[0].axhline(0.3, color='red')
ax[0].axhline(0.4, linestyle='--', color='blue')
ax[0].axhline(0.5, color='cyan', linewidth=10)
ax[0].axhline(0.6, linestyle=':', color='orchid', xmin=0.25, xmax=0.75)
ax[0].axhline(0.7, xmin=0.25, xmax=0.75, color=(0.1, 0.2, 0.5, 0.3))

ax[1].axvline(0.3, color='red')
ax[1].axvline(0.4, linestyle='--', color='blue')
ax[1].axvline(0.5, color='cyan', linewidth=10)
ax[1].axvline(0.6, linestyle=':', color='orchid', ymin=0.25, ymax=0.75)
ax[1].axvline(0.7, ymin=0.25, ymax=0.75, color=(0.1,0.2,0.5,0.3))

fig.tight_layout()

# COMMAND ----------

x = np.array([2,4,6,7,4,2,5,7,8,9,4,2,1])
y = np.array([7,5,4,1,6,7,8,1,9,5,9,3,5])

fig, ax = plt.subplots(1,3)
ax[0].scatter(x,y)
ax[0].set_title('default')

ax[1].scatter(x,y)
ax[1].set_title('size = 50, style = +')

crosses = ax[2].scatter(x, y, 200, marker='+', linewidth=3)
bullets = ax[2].scatter(x, y, 50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

fig.tight_layout()

# COMMAND ----------

z = np.array([0,1,4,3,5,1,2,5,7,5,9,8,5])
fig = plt.figure()

ax = np.array([fig.add_subplot(1, 3, 1, projection= '3d'),
               fig.add_subplot(1, 3, 2, projection= '3d'),
               fig.add_subplot(1, 3, 3, projection= '3d')])

ax[0].scatter(x,y,z)
ax[0].set_title('default')

ax[1].scatter(x, y, z, s=50, marker='+')
ax[1].set_title('size=50, style=+')

crosses = ax[2].scatter(x, y, 200, marker='+', linewidth=3)
bullets = ax[2].scatter(x, y, 50, marker='o', color='black')
bullets.set_edgecolors('red')
bullets.set_linewidth(1.5)
ax[2].set_title('mixed')

# COMMAND ----------

people = ["Student A", "Student B"] # data
studentA = np.array([90,50,80,40])
studentB = np.array([75,45,60,95])
x = np.arange(len(studentA))

fig, ax = plt.subplots(1,2) # figure

ax[0].bar(x, studentA, width=0.3) # plots
ax[1].bar(x, studentB, width=0.3)

for i in range(len(ax)):
    ax[i].set_ylim([0, 100])
    ax[i].set_title(people[i])
    ax[i].set_xlabel("exercises")
    ax[i].set_ylabel("mark (%)")
    ax[i].set_xticks([0,1,2,3])
    ax[i].set_xticklabels(["ex1", "ex2", "ex3", "ex4"])
    
fig.tight_layout()

# COMMAND ----------

people = ["Student A", "Student B"] # data
studentA = np.array([90,50,80,40])
studentB = np.array([75,45,60,95])
x = np.arange(len(studentA))

fig, ax = plt.subplots()
width = 0.3
s1bars = ax.bar(x - width/2, studentA, width, label='student A', color='black')
s2bars = ax.bar(x + width/2, studentB, width, label='student B', color='blue')


ax.set_title("Bar charts on same graph")
ax.set_ylim(0, 100)
ax.set_xlabel("independent variable")
ax.set_ylabel("number of victims or whatever")
ax.legend()
ax.set_xticks([0,1,2,3])
ax.set_xticklabels(["ex1", "ex2", "ex3", "ex4"])


for i in range(len(studentA)):
    s1bars[i].set_linewidth(3.5)
    s2bars[i].set_linewidth(3.5)
    if studentA[i] < 50:
        s1bars[i].set_edgecolor('red')
    if studentB[i] < 50:
        s2bars[i].set_edgecolor('red')
        

fig.tight_layout()

# COMMAND ----------



