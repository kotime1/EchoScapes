from api.spotify import *
import pandas as pd
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