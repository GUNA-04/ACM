import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\techn\\Documents\\GitHub\\ACM\\Recruitment\\ML\\Unsupervised\\sales.csv")

numbers = ['Price', 'Quantity Sold', 'RAM', 'ROM']
data_numbers = data[numbers].copy()

data_numbers['RAM'] = data_numbers['RAM'].str.replace('GB', '', regex=False).astype(float)
data_numbers['ROM'] = data_numbers['ROM'].str.replace('TB', '000', regex=False).str.replace('GB', '', regex=False).astype(float)

scaler = StandardScaler()
scaled = scaler.fit_transform(data_numbers)

kmeans = KMeans(n_clusters=3, random_state=42)
groups = kmeans.fit_predict(scaled)

data['Group'] = groups

plt.scatter(data_numbers['Price'], data_numbers['Quantity Sold'], c=groups, cmap='viridis')
plt.xlabel('Price')
plt.ylabel('Quantity Sold')
plt.title('Mobile Sales Clustering')
plt.colorbar(label='Cluster Group')
plt.show()

print(data.groupby('Group').mean(numeric_only=True)[['Price', 'Quantity Sold', 'RAM', 'ROM']])