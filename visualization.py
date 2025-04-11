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

# #bar plots:
# x = [1, 3, 5, 7, 9]
# y = [9, 4, 6, 8, 3]
# plt.bar(x,y)
# plt.show()

# #barchart with categorical x values:
# x = ["Europe", "Canada", "India", "USA", "China"]
# y = [9, 4, 6, 8, 3]
# plt.bar(x,y)
# plt.show()

# #Multiple Bar Graphs:
# x = [1,3,5,7,9]
# x1 = [2,4,6,8,10]
# y = [9, 4, 6, 8, 3]
# y1 = [6,5,9,7,10]
# plt.bar(x1,y,color = "pink")
# plt.bar(x,y1,color = "blue")
# plt.xticks(ticks = x, labels = ["Europe" , "Canada", "India", "USA", "China"])
# plt.show()

#Histrograms:
bob = np.random.randint(20, 60, 100)
daniel = np.arange(20, 60, 5)
plt.hist(bob, daniel, edgecolor = "darkblue")
plt.show()

#ScatterPlot:
x = [4,5,7,10,11]
y = [2,1,7,6,12]
plt.scatter(x,y,marker = "*", s = 20, color = "darkred")
plt.show()

#Stackplot:
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday" , "Saturday", "Sunday"]
Studying = [2, 3, 2, 0, 1, 4, 5,]
Reading = [1, 2, 1, 3, 1, 2, 2]
Listening_to_music = [3, 2, 4, 2, 3, 1, 1]
Singing = [2, 3, 1, 4, 5, 2, 1]
plt.stackplot(days, Studying, Reading, Listening_to_music, Singing, labels = ["Studying", "Reading","Listening To Music","Singing"],colors = ["lightblue","lightpink","lightgreen","lightyellow"])
plt.legend()
plt.show()

#Subplots:
plt.subplot(2, 3, 1)
plt.stackplot(days, Studying, Reading, Listening_to_music, Singing, labels = ["Studying", "Reading","Listening To Music","Singing"],colors = ["lightblue","lightpink","lightgreen","lightyellow"])
plt.subplot(2, 3, 2)
plt.pie(slices, labels = labels,autopct='%1.0f%%',startangle = 90, colors = ["lightblue","lightpink","lavender", "lightgreen","lightyellow"], shadow = True)
plt.subplot(2,3,3)
plt.scatter(x,y,marker = "*", s = 20, color = "darkred")
plt.subplot(2,3,4)
plt.hist(bob, daniel, edgecolor = "darkblue")
plt.show()

#PieChart:
slices = [4,5,7,10,11]
labels = ["bananas","strawberry","dragonfruit","papaya","pear"]
plt.pie(slices, labels = labels,autopct='%1.0f%%')
plt.show()
