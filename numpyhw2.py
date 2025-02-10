import numpy as np

eq = input("Hello! Okay, were gonna do some equation solving. Pick, is your question a linear question (ax+b), or quadratic (ax^2+bx+c)? ")

if(eq == "Linear"):
    a = int(input("Okay, enter a value for a: "))
    b = int(input("Okay, enter a value for b: "))
    x = int(input("Okay, enter a value for x: "))
    ans = a*x + b
    print("so, (", a, "x", x ,") +" ,b ,"=", ans)

elif(eq == "Quadratic"):
    a2 = int(input("Okay, enter a value for a: "))
    b2 = int(input("Okay, enter a value for b: "))
    c2 = int(input("Okay, enter a value for c: "))
    x2 = int(input("Okay, enter a value for x: "))
    ans2 = a2*x2**2 + b2*x2 + c2
    print("so, (", a2 , "x" , x2 , "²) + (" , b2 , "x" , x2 , ") +" , c2 , "=" , ans2)

else:
    print("Sorry, We didnt quite understand that.")

print('thank you for using this service!')
