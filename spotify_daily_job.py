from os import environ
from io import BytesIO
from SpotifyAPI import recently_played_df
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload


# GCS Configs
creds = service_account.Credentials.from_service_account_info(
    environ.get("SPOTIFY_RECENTLY_PLAYED")
)
bucket_name = environ.get("BUCKET_NAME")
service = build("storage", "v1", credentials=creds)

# Filtering Today's ---->
today_date = datetime.datetime.today().strftime("%Y-%m-%d")
recently_played = recently_played_df()
print(f"\n [!] Filtering out Today's Data {today_date}.")
recently_played = recently_played[
    recently_played["played_at"].dt.strftime("%Y-%m-%d") == today_date
]
# End Of Filtering ----->

# Converting the parquet file to Bytes Stream
stream = BytesIO()
recently_played.to_parquet(stream, index=False)

stream.seek(0)  # seek(0) makes the stream to read mode.

# Pushing parquet file to GCS bucket
media = MediaIoBaseUpload(stream, mimetype="application/octet-stream")
blob_name = f"{today_date}.parquet"
destination_blob_name = f"recently_played/{blob_name}"
req = service.objects().insert(
    bucket=bucket_name, name=destination_blob_name, media_body=media
)
resp = req.execute()
