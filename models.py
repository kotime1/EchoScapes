from sklearn.cluster import KMeans
from preprocessor import *

# Select features for clustering
X = merged_df[numeric_cols]

# Train KMeans model
kmeans = KMeans(n_clusters=4, random_state=42)
merged_df['cluster'] = kmeans.fit_predict(X)

# Visualize the clusters
print(merged_df[['track_name', 'artist_name', 'cluster']].head())

# Example: Generate prompts based on clusters
def generate_prompt(row):
    if row['cluster'] == 0:
        return "A calm, serene landscape with soft colors."
    elif row['cluster'] == 1:
        return "A vibrant cityscape with neon lights."
    # Add more prompts for different clusters

merged_df['dalle_prompt'] = merged_df.apply(generate_prompt, axis=1)
print(merged_df[['track_name', 'dalle_prompt']].head())
