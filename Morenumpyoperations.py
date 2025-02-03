import numpy as np

helda = np.arange(-4, 18, 2)
print(helda)

#Slicing 

print(helda[3 : 8])
print(helda[:5])
print(helda[4:])

print(helda[1:9:2]) #start, stop, step
print(helda[10:3:-2]) #if my step is negative, it gives me my array in reverse order
print(helda[::-1]) #reverses the whole array

#Slicing a 2D array

peter = np.arange(2, 26, 2)
bob = peter.reshape((3,4))
print(bob)

print(bob[0:2 , 1:3]) #Startrow : Endrow , Startcolumn : Endcolumn

#Selecting Indices

print(helda[[1,3,6]])

#Conditional Slicing  

print(helda[helda%3 == 0]) # % = Finding the reminder

print(bob[bob >= 15])

#Evaluating an expression

x = np.arange(3,10)
print(x)

y = 2*x + 5
print(y)