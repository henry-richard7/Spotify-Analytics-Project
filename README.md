# Spotify-User-Specific-Data
This repos uses github actions to get my recently played songs and add it as a parquet file in GCS Bucket.

# How to use?

* Sign Up for a spotify developer account from [Here](https://developer.spotify.com/)
* After Sign Up go to [Dashboard](https://developer.spotify.com/dashboard/)
* Click on Create An App. Give it a name and description and click on create App.
* Copy your Client Secret and Client ID and create a secret for github in **Settings -> Secrets -> Actions** as below
  - **SPOTIFY_CLIENT_ID:** Your Spotify Client ID.
  - **SPOTIFY_CLIENT_SECRET:** Your Spotify Client Secret.
* After that run **get_spotify_refresh_token.py** file in your local and follow the steps.
* Copy your refresh token and create a secret for github in **Settings -> Secrets -> Actions** as below
  - **SPOTIFY_REFRESH_TOKEN:** The refresh token you got after running **get_spotify_refresh_token.py**.

# GCS (Google Cloud Storage) Bucket:
* GCP provides 5GB Free GCS bucket when you create App Engine service.(completely free no need billing)
* Before creating GCS bucket App Engine service make sure to create a service account with Storage Admin Role for the same. follow Step of the [Guide](https://support.google.com/a/answer/7378726?hl=en)
* After completing the above step in Google Cloud Console search for App Engine and enable it.
* After enabling you will get 2 GCS buckets your-project-id.appspot.com and staging.your-project-id.appspot.com we don't need staging bucket.
* Copy your GCS bucket name and create a secret for github in **Settings -> Secrets -> Actions** as below
   - **BUCKET_NAME:** The name of your GCS Bucket.
* Run **encode_service_account.py** in your local to encode the service account json file you got and copy the encoded string and create a secret for github in **Settings -> Secrets -> Actions** as below
  - **SPOTIFY_RECENTLY_PLAYED:** The encoded string you got after running **encode_service_account.py**
