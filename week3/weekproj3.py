import matplotlib.pyplot as plt 
from sklearn.preprocessing import MinMaxScaler 
from sklearn.preprocessing import StandardScaler 
import pandas as pd  
data=pd.read_csv("data.csv") 
print(data) 
print("Min Max Scaler") 
numeric_col=data.select_dtypes(include='number').columns 
scaler=MinMaxScaler() 
data_normalized=pd.DataFrame(scaler.fit_transform(data[numeric_col]),columns=numeric_col) 
print(data_normalized.head()) 
print("data Scaler") 
numeric_col1=data.select_dtypes(include="number").columns 
scaler=StandardScaler() 
data_standardized=pd.DataFrame(scaler.fit_transform(data[numeric_col1]),columns=numeric_col1) 
print(data_standardized.head()) 
plt.figure(figsize=(8,6)) 
plt.hist(data['Avg_Price'],bins=10) 
plt.title("Distribution of Sales", ) 
plt.xlabel("Avg_Price") 
plt.ylabel("Frequency") 
plt.show() 
 
 
