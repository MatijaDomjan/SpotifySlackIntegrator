import datetime
from datetime import datetime

import pandas as pd
import requests

CLIENT_ID = ''  # insert your CLient ID
CLIENT_SECRET = ''  # insert your Client secret
AUTH_URL = 'https://accounts.spotify.com/api/token'
TOKEN = ''


def generate_headers():
    tok = post()
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }
    return headers


def request_to_spotify():
    headers = generate_headers()
    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=5)  # for last 5 days
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000
    data = requests.get(
        "https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp),
        headers=headers)
    data = data.json()
    return data


def extract_data():
    list_of_song = []
    list_of_time_played = []
    list_of_artist = []
    list_of_albums = []
    data = request_to_spotify()
    for song in data['items']:
        list_of_song.append(song['track']['name'])
        list_of_time_played.append(song['played_at'])
        list_of_artist.append(song['track']['artists'][0]['name'])
        list_of_albums.append(song['track']['album']['name'])
    return list_of_song, list_of_time_played, list_of_artist, list_of_albums


def transform_data():
    list_of_song, list_of_time_played, list_of_artist, list_of_albums = extract_data()
    frame = pd.DataFrame(
        {'Song': list_of_song,
         'time_played': list_of_time_played,
         'name': list_of_artist,
         'album': list_of_albums
         })
    print(frame)


if __name__ == "__main__":
    transform_data()







