import requests


token_url = "https://open.spotify.com/get_access_token?reason=transport&productType=web_player"
response = requests.get(token_url).json()
token = response["accessToken"]


def artist_meta(artist_id: str):
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    response = requests.get(url,headers={"Authorization": f"Bearer {token}"}).json()
    result = response

    try:
        artist_image = result["images"][1]["url"]
    except:
        artist_image = None

    try:
        geners = result["genres"][0]
    except:
        geners = None

    return {"artist_image": artist_image, "genres": geners}
