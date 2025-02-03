import numpy as np

num = [1,26,39,805,0]
print(num)
print(type(num))

#Converting a list into an array
numarr = np.array(num)
print(numarr)
print(type(numarr))

#doubling with a list
for n in range(len(num)):
    num[n] = num[n]*2

print(num)

#doubling with an array
print(numarr*2)

#An array of 0
zero = np.zeros(3, int)
print(zero)

#two dimentional zero array
zero2 = np.zeros((3,4), int)
print(zero2) 

#ones array
one = np.ones((2,4,3))
print(one)

#Finding the dimention of an array
print(one.ndim)
print(zero.ndim)
print(zero2.ndim)

#finding the shape of an array
print(one.shape)
print(zero.shape)
print(zero2.shape)

#finding the size of an array
print(one.size)
print(zero.size)
print(zero2.size)

#Array with numbers in range x
sofia = np.arange(1,10,2) #Start, Stop, Step
print(sofia)

#changing the arrangement of an array
print(np.random.permutation(sofia))
print(np.random.permutation(sofia))
print(np.random.permutation(sofia))

#array with random numbers
print(np.random.randint(1,11,7)) #start, end, number of values
print(np.random.randint(-7, 9 , (3,4))) #start,end,rowsandcolumns

print(hi)

#reshaping an array (changing the rows and columns)

hi2 = hi.reshape((2,6)) #Total number of items in the original array have to be equal to the total number of items in the reshaped array

print(hi2)

#sorting (arranging items in increasing or decreasing order)
print(hello)
hello2 = np.sort(hello)
print(hello2)


