import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#To find your client_id and client secret I refer you to https://developer.spotify.com/documentation/general/guides/app-settings/
#In addition this may be of use as well:https://spotipy.readthedocs.io/en/2.13.0/#

#Fill in this stuff
SPOTIPY_CLIENT_ID='enter_client_id'
SPOTIPY_CLIENT_SECRET='enter_client_secret'
playlist_id = 'enter_playlist_id'
output_directory = r"C:\Users\User_name\Documents"

client_credentials_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID,SPOTIPY_CLIENT_SECRET)
sp = spotipy.client.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.playlist(playlist_id)

#Downloads the cover art from the playlist you specified

for i in range(len(results["tracks"]["items"])):
    a = results["tracks"]["items"][i]["track"]
    cover_art_url = a["album"]["images"][0]["url"]
    artist_name   = a["album"]["artists"][0]["name"]
    song_name     = a["name"]
    
    file_name = artist_name + " - " + song_name + ".jpg"
    img_data = requests.get(cover_art_url).content
    
    file_path = file_path = os.path.join(output_directory, file_name)
    with open(file_path, 'wb') as handler:
        handler.write(img_data)

