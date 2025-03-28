import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,11)
y = 2*x

#Line Plot:
# plt.figure(figsize = (7,5))
# plt.plot(x,y,'m-..',linewidth = 1, markersize = 6 , label = "x² + 2x + 3 = y")
# plt.legend()
# plt.title("The responsiveness of supply to price for apples:")
# plt.xlabel("Number of apples sold")
# plt.ylabel("Price")
# plt.xticks(ticks = x , labels = x)
# #plt.xticks(ticks = x , labels = [2, 6, 70, 80, 20, 305, 68, 0, 935, 6, 79])
# plt.axis([0,20 , 0, 50])
# #plt.show()

#multiple plots
x1 = np.arange(0,10,0.1)
y1 = x1**2
y2 = x1**3
plt.plot(x1,y1,'y-.',linewidth = 1,markersize = 6, label = "x² = y")
plt.plot(x1,y2,'r-.',linewidth = 1,markersize = 6, label = "x³ = y")
plt.legend()
plt.show()
