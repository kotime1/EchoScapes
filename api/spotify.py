import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='your_spotify_client_id',
                                               client_secret='your_spotify_client_secret',
                                               redirect_uri='http://localhost:8888/callback',
                                               scope="user-top-read user-read-recently-played"))

# Fetch user's top tracks
top_tracks = sp.current_user_top_tracks(limit=50, time_range='long_term')

# Extract track information
track_data = []
for item in top_tracks['items']:
    track_info = {
        'track_name': item['name'],
        'artist_name': item['artists'][0]['name'],
        'popularity': item['popularity'],
        'album': item['album']['name'],
        'release_date': item['album']['release_date'],
        'track_id': item['id'],
    }
    track_data.append(track_info)

# Convert to DataFrame
track_df = pd.DataFrame(track_data)
print(track_df.head())

# Get audio features for the top tracks
audio_features = []
for track_id in track_df['track_id']:
    features = sp.audio_features(track_id)[0]
    audio_features.append(features)

# Convert to DataFrame
features_df = pd.DataFrame(audio_features)

# Merge with track info
merged_df = pd.concat([track_df, features_df], axis=1)

# Preprocess (e.g., normalize, handle missing data)
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numeric_cols = ['tempo', 'energy', 'valence', 'danceability']
merged_df[numeric_cols] = scaler.fit_transform(merged_df[numeric_cols])

print(merged_df.head())

from sklearn.cluster import KMeans

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
