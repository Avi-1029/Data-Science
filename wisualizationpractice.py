import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

titanic = pd.read_csv("C:\\Users\\Biju\\Desktop\\Jetlearn\\Data Science\\Resources\\titanic.csv")

cls = titanic.groupby("Pclass")
name = cls.count()["Name"]

x = name.index
plt.bar(x, name)
plt.xticks(ticks = x, labels = x)
plt.show()

bins = np.arange(0, 100, 10)
ages = titanic["Age"]
plt.hist(ages, bins, edgecolor = "darkblue")
plt.show()


iris = pd.read_csv("C:\\Users\\Biju\\Desktop\\Jetlearn\\Data Science\\Resources\\iris.csv")          

print(iris.info())
spcs = iris.groupby("species")
spcsss = spcs.count()
bob = spcsss["sepal_width"]
labels = spcsss.index
plt.pie(bob,labels=labels, autopct='%1.0f%%',startangle = 90, colors = ["lightpink","lavender","lightyellow"], shadow = True)
plt.show()

x = iris["petal_length"]
y = iris["petal_width"]
plt.scatter(x,y,marker = "x")
plt.show()