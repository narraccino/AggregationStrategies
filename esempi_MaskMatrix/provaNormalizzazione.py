from sklearn import preprocessing
import pandas as pd


data = [1, 2, 5, 6, 0, 10, 10]
r= pd.DataFrame(data).values.astype(float)
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(r.reshape(-1,1))
df_normalized = pd.DataFrame(x_scaled)

print(df_normalized)