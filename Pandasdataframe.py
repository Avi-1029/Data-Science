import pandas as pd

Bob = {"Animals:" : ["Lion" ,"Tiger", "Giraffe", "Kangaroo", "Polar Bear"] , "Birds:" : ["Eagle" , "Crow", "Pigeon", "Peacock", "Dove"]}
Bobby = pd.DataFrame(Bob)
#print(Bobby)

#Reading data from CSV
titanic = pd.read_csv("C:\\Users\\Biju\\Desktop\\Jetlearn\\Data Science\\Resources\\titanic.csv")
print(titanic)

#Displaying the first few rows
print(titanic.head())

#Displaying the last few rows
print(titanic.tail())

#Finding the number of rows and columns
print(titanic.shape)

#Extracting values of one column
fare = titanic["Fare"]

#Mean Fare:
print(fare.mean())

#What are the different passenger classes:
pclass = titanic["Pclass"]
print(pclass.value_counts())

#Summary of the data:
print(titanic.info())

#Statistical summary of data set
print(titanic.describe())