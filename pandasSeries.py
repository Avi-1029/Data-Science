import pandas as pd

bob = [3, 89, -2, 17, 54, 246, -390, 17, 89]
print(bob)
print(type(bob))
bobjr = pd.Series(bob)
print(bobjr)
print(type(bobjr))

#Getting the value of a secific index:

print(bobjr[3])

#Statastical funtions:

print(bobjr.sum()) #Sum of all values in a series
print(bobjr.min()) #Smallest number of a series
print(bobjr.max()) #Biggest value of a series
print(bobjr.mean()) #Mean value
print(bobjr.median()) #Median value 
print(bobjr.mode()) #Most repeated value in a series

#Count of unique values 

print(bobjr.value_counts()) 

#Sorting series' (ascending to decending)

print(bobjr.sort_values())
print(bobjr.sort_values(ascending = False))