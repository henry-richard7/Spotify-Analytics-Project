import requests
from urllib.parse import urlparse, parse_qs

scopes = "user-read-recently-played"
client_id = input('Your Spotify Client ID: ')
client_secret = input('Your Spotify Client Secret: ')
redirect_url = input('Your Spotify Redirect Uri that you have entered in Edit Settings in Dashboard: ')

url = f"https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&scope={scopes}&redirect_uri={redirect_url}"
print(f"Go To This Url: {url}")
input_code = input("Enter the URL you got after login to spotify: ")
parsed_url = urlparse(input_code)
code = parse_qs(parsed_url.query)['code']
    
token_url = "https://accounts.spotify.com/api/token"
body = {
        "code": code,
        "redirect_uri": redirect_url,
        "grant_type": "authorization_code",
    }
    
response = requests.post(token_url, data=body, auth=(client_id, client_secret)).json()
print(response['refresh_token'])