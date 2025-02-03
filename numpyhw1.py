import numpy as np

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

rn = [a,b]
nmp = np.array(rn)

c = int(input("Enter a number :"))
d = int(input("Enter another Number: "))

mr = [c,d]
nrp = np.array(rn)

print(nrp + nmp)