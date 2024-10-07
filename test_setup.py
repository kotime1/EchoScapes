import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
# OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET, redirect_uri="http://localhost:8000", scope="user-top-read"))

# Fetch user data
user = sp.current_user()
print(f"Logged in as {user['display_name']}")