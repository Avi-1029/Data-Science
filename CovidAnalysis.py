import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

covid = pd.read_csv("C:\\Users\\Biju\\Desktop\\Jetlearn\\Data Science\\Resources\\covid_data.csv")

print(covid.info())
covid = covid[['Province_State', 'Country_Region', 'Confirmed', 'Recovered', 'Deaths']]
print(covid)
print(covid.isnull().sum())
covid.fillna(value = "", inplace = True)
print(covid.isnull().sum())

#Scatter plot for top ten most affected countries:

bob = covid.groupby('Country_Region')
harry = bob.sum()
ttc = harry.sort_values("Confirmed", ascending = False).head(10)
print(ttc)

x = ttc.index
y = ttc['Confirmed']
plt.scatter(x, y, marker = "*", s = 20, color = "darkred")
plt.show()

#Bar plot for top ten countries with highest deaths:

kevin = harry.sort_values("Deaths", ascending = False).head(10)
x = kevin.index
y = kevin['Deaths']
plt.bar(x, y, 0.9, edgecolor = "black")
plt.show()

#Country:

print(covid['Country_Region'].value_counts())
spain = covid[covid['Country_Region'] == "Spain"]

top10spain = spain.sort_values("Confirmed", ascending = False).head(10)
x = top10spain['Province_State']
y = top10spain['Confirmed']
plt.bar(x, y, 0.9 , edgecolor = 'black')
plt.show()
