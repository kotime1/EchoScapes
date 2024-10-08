from ingester import *

# Preprocess (e.g., normalize, handle missing data)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numeric_cols = ['tempo', 'energy', 'valence', 'danceability']
merged_df[numeric_cols] = scaler.fit_transform(merged_df[numeric_cols])

print(merged_df.head())
