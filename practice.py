import pandas as pd
iris = pd.read_csv("C:\\Users\\Biju\\Desktop\\Jetlearn\\Data Science\\Resources\iris.csv")
print(iris)

pl = iris["petal_length"]
pw = iris["petal_width"]
print(pl.min(), "\n" , pl.max())
print(pw.min(), "\n" , pw.max())

sp = iris.groupby("species")
spn = sp.mean()

print(spn[["sepal_length" , "sepal_width"]])

iris["species"] = iris["species"].str.upper()
print(iris)