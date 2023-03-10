import requests
import pandas as pd
import datetime
from artist_meta import artist_meta
from os import environ

Previous_Date = datetime.datetime.today() - datetime.timedelta(days=1)

client_id = environ.get("SPOTIFY_CLIENT_ID")
client_secret = environ.get("SPOTIFY_CLIENT_SECRET")


refresh_token_url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "refresh_token", "refresh_token": environ.get('SPOTIFY_REFRESH_TOKEN')}
res = requests.post(
            refresh_token_url, auth=(client_id, client_secret), data=data
).json()

access_token=res["access_token"]
headers = {"Authorization": f"Bearer {access_token}"}

def audio_features(track_id):
     url = f"https://api.spotify.com/v1/audio-features/{track_id}"
     return requests.get(url,headers=headers).json()

def recently_played_df():
    url = "https://api.spotify.com/v1/me/player/recently-played?limit=50"
    

    recently_played = requests.get(url,headers=headers).json()
    results = []
    print("[*] Fetching Recently Played Songs From API........")
    for r in recently_played["items"]:
        track_meta = audio_features(r["track"]["id"])
        artist_metas = artist_meta(r["track"]["artists"][0]["id"])
        results.append(
            {
                "song": r["track"]["name"],
                "track_id": r["track"]["id"],
                "album_name": r["track"]["album"]["name"],
                "album_art": r["track"]["album"]["images"][0]["url"],
                "artist": r["track"]["artists"][0]["name"],
                "artist_id": r["track"]["artists"][0]["id"],
                "release_date": r["track"]["album"]["release_date"],
                "duration": r["track"]["duration_ms"],
                "preview_url": r["track"]["preview_url"],
                "explicit": "Explicit Content"
                if r["track"]["explicit"]
                else "Non Explicit Content",
                "played_at": r["played_at"],
                "artist_image": artist_metas["artist_image"],
                "genres": artist_metas["genres"],
                "danceability": track_meta["danceability"] if track_meta else 0,
                "energy": track_meta["energy"] if track_meta else 0,
                "key": track_meta["key"] if track_meta else 0,
                "loudness": track_meta["loudness"] if track_meta else 0,
                "mode": track_meta["mode"] if track_meta else 0,
                "speechiness": track_meta["speechiness"] if track_meta else 0,
                "acousticness": track_meta["acousticness"] if track_meta else 0,
                "instrumentalness": track_meta["instrumentalness"] if track_meta else 0,
                "liveness": track_meta["liveness"] if track_meta else 0,
                "valence": track_meta["valence"] if track_meta else 0,
                "tempo": track_meta["tempo"] if track_meta else 0,
            }
        )

    df = pd.DataFrame(results)
    df["release_date"] = pd.to_datetime(df["release_date"])
    df["played_at"] = pd.to_datetime(df["played_at"])
    print("[-] Completed API Fetch.")
    return df
