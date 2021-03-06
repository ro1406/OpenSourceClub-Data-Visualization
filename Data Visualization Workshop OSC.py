# -*- coding: utf-8 -*-
"""Data Viz Workshop OSC.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/120nug0eNShRQ5OTilOxuQJSVfmkigRxw

@Author: Rohan Mitra b00085023@aus.edu
"""
#################################
## SECTION 1 - Matplotlib
#################################
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,10)
y = x**2   # x*x
print("x=",x)
print("y=",y)

plt.plot(x,y)
plt.show()

plt.plot(x,y)#Always called at the start
plt.xlabel("x") #The name of the x label
plt.ylabel('y') #The name of the y label
plt.title("y=x^2") #The title
plt.show()  # Always called at the END

plt.plot(x,x**2, "red")
plt.plot(x,x**3, 'blue')
plt.xlabel("X axis")
plt.ylabel('Y axis')
plt.title("Plotting something")
plt.show()

plt.plot(x,x**2)
plt.plot(x,x**3)
plt.xlabel("X axis")
plt.ylabel('Y axis')
plt.title("Plotting something")
plt.legend( ["y=x^2" , "y=x^3" ] , loc=2 )
plt.show()

x1=np.linspace(1,50,100)  # 1 to 50, with 100 points in between
print(x1)

y=x1+3*np.random.randn(len(x1)) #for show only
plt.scatter(x1,y)  # When you dont wanna connect the dots
plt.show()

plt.step(x,x**2) #if numbers map to whole numbers ( Discrete mappings )
plt.plot(x,x**2)
plt.legend( [ "step plot","line plot" ] )
plt.show()

plt.fill_between(x,x**2,x**3, color="r")
plt.show()

#################################
## SECTION 2: Seaborn:
#################################
import seaborn as sns

data = sns.load_dataset('tips')

print(data.head())  #First 5 rows of our data

print(data)

data['tip'].describe() #Numerical & Categorical

print(data.info())

# Distribution plot
# Numerical columns only
sns.distplot( data[ 'total_bill' ] ) # [] are to tell python im gonna call the columns

# Joint plot
# numerical vs numerical
sns.jointplot(x=data['tip'] , y=data['total_bill'])#, data=data)

sns.jointplot(x='tip' , y='total_bill' , data=data, hue='day') #hue of a categorical column

sns.jointplot(x='tip' , y='total_bill' , data=data, kind='hex')
# Darkness of hexagons show you the density of the number of observations in that region

sns.jointplot(x='tip' , y='total_bill' , data=data, kind='kde')  # DROP THIS

sns.jointplot(x='tip' , y='total_bill' , data=data, kind='reg') #regression

#################################
## SECTION 3: Categorical Plots:
#################################

sns.pairplot(data, hue='sex')

# Categorical vs Numerical
sns.barplot(x='sex',y='total_bill',data=data)  #Mean values

sns.barplot(x='sex',y='total_bill',data=data, estimator=np.std) #standard deviation Could be omitted

# categorical
sns.countplot(x='day',data=data)

plt.figure( figsize=(12,10) )
sns.boxplot(x='day', y='total_bill',data=data) #categorical X numerical


#################################
## SECTION 4: Matrix Plots
#################################

print(data.corr()) # how are the columns of my data related?

# Heatmap
# inside () put a table
sns.heatmap( data.corr() ,cmap='coolwarm') #cmap changes color scheme

flights = sns.load_dataset('flights')

print(flights.head())

print(flights.describe())

table = flights.pivot_table(values='passengers',columns='year', index='month')
print(table)

plt.figure(figsize=(12,10))
sns.heatmap( table)#, annot=True, lw=2)

sns.clustermap( table ) #,annot=True
#wanna go from map to axes.

