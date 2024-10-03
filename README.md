# 🎧 EchoScapes 🎨

Spotify Art Generator is a Python-based project that reads your Spotify listening data, analyzes your music preferences using machine learning, and generates unique, personalized artwork with DALL·E 3 based on your listening habits.

## Features

* Fetches data from the Spotify API, including top tracks, artists, genres, and audio features.
* Uses machine learning to analyze and learn from your music preferences.
* Automatically generates creative image prompts based on your music stats and feeds them to DALL·E 3.
* Displays generated images that visually represent your musical taste.

## Architecture Overview

```
EchoScapes/
├── README.md
├── config/
├── data/
├── models/
├── notebooks/
├── src/
├── api/
├── templates/
├── static/
├── requirements.txt
├── docker-compose.yml
├── Dockerfile
├── tests/
└── deployment/
```

* **Spotify API Integration**: Pulls Spotify listening data such as top tracks, genres, and detailed song features like energy, tempo, and valence.
* **Machine Learning Model**: Learns your music preferences and identifies patterns based on Spotify stats.
* **DALL·E 3 Integration**: Generates custom artwork based on music preferences and listening habits.

## Getting Started

### Prerequisites

* **Spotify API Developer Account**: You'll need to register your app and get credentials from [Spotify for Developers](https://developer.spotify.com/).
* **OpenAI API Key**: Sign up for DALL·E 3 access through OpenAI.
* **Python**: Version 3.8 or higher.
* **Docker (Optional)**: For easier deployment.

### Installation

1. Clone the repository:

```sh
git clone https://github.com/kotime1/EchoScapes.git
cd EchoScapes
```

2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

3. Setup configurations

* Rename ```config/secrets_template.json``` to ```secrets.json``` and fill in your Spotify API and OpenAI API keys.

```json
{
  "SPOTIFY_CLIENT_ID": "your_spotify_client_id",
  "SPOTIFY_CLIENT_SECRET": "your_spotify_client_secret",
  "OPENAI_API_KEY": "your_openai_api_key"
}
```

### Usage

#### Step 1: Fetch Spotify Data

Use the script to fetch your Spotify stats:

```sh
python src/spotify_client.py
```

This will retrieve your top tracks, artists, and audio features and store them in ```data/spotify_data.json```.

#### Step 2: Train the Machine Learning Model

Once the data is fetched, you can train the model that will learn your preferences:

```sh
python src/ml_model.py
```

#### Step 3: Generate Art

Once the model is trained and prompts are generated, run the image generation:

```
python src/image_generator.py
```

Your personalized artwork will be generated and saved in the ```static/images/``` folder.

### API

Optionally, you can deploy the project as a web app using Flask/FastAPI.

1. Run the app:

```sh
python api/app.py
```

2. Access the API at http://localhost:5000 to generate images via HTTP requests.

### Docker Deployment

For an easy setup, use Docker to run the app in a containerized environment:

```sh
docker-compose up --build
```

### File Structure

* ```config/```: Contains app settings and API keys.
* ```data/```: Spotify data and preprocessed stats.
* ```models/```: Trained machine learning models.
* ```src/:``` Main project scripts, including Spotify API interactions, data processing, ML model, and DALL·E prompt generation.
* ```api/```: API endpoints for web app deployment.
* ```templates/```: HTML templates for the frontend (if using a web interface).
* ```static/```: Generated images and static assets.
* ```tests/```: Unit tests for Spotify API client and machine learning model.
* ```deployment/```: Docker, NGINX, and optional Kubernetes configurations.

### Future Features

* **Playlist-based Generation**: Generate images based on individual playlists.
* **Real-time Updates**: Automatically update images as you listen to more music.
* **User Customization**: Customize the styles and colors based on personal preferences.

Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue if you have any suggestions or bug reports.
License

This project is licensed under the MIT License. See the LICENSE file for details.
