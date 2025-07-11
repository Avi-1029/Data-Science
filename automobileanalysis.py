import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import LabelEncoder

amb = pd.read_csv(r"C:\Users\Biju\Desktop\Jetlearn\Data Science\Resources\automobile_sales_data_with_orders.csv")

print(amb.info)
print(amb.isnull().sum())

print(amb['Car Model'].value_counts())

#Encoding values
le = LabelEncoder()
amb['Month'] = le.fit_transform(amb['Month'])
amb['Car Model'] = le.fit_transform(amb['Car Model'])
print(amb['Car Model'])

# #Seperating features and targets:

x = amb[['Month', 'Car Model', 'Opening Stock', 'Units Sold', 'Closing Stock', 'Orders in Waiting']]
y = amb['Units Ordered (Next Month)']