import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

covid = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Resources\WHO-COVID-19-global-data.csv")
print(covid.info())

covid['DateReported'] = pd.to_datetime(covid['DateReported'])
print(covid.info())

#Scatter Plot Total Daily Cases Worldwide:
covid1 = covid.groupby('DateReported').sum()
x = covid1.index
y = covid1['Cumulative_cases']
plt.scatter(x, y, marker = "*", s = 20, color = "darkred")
#plt.show()

#Scatter Plot New Cases Worldwide:
x = covid1.index
y = covid1['New_cases']
plt.plot(x,y, color = "darkred" )
#plt.show()

covid['Year'] = covid['DateReported'].dt.year

covid['Month'] = covid['DateReported'].dt.month_name()
print(covid)

#Line Plot for Total Deaths:

bob = covid.drop(columns = 'DateReported').groupby(['Year','Month']).sum()
print(bob)
x = bob.index
y = bob['Cumulative_deaths']
print(x)
print(y)
plt.bar(x,y,color = 'black')
plt.show()