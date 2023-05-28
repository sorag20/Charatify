import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify APIのクライアント情報
client_id = 'e9e1721fa9c44d38a8d44ab7f7418315'
client_secret = 'ad0ccafab2d3470984903e0a0da6ef4c'

# Spotifyクライアントを作成
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 日本のトップ１０の曲を出力
def get_top10_tracks():
    # 日本のトップトラックのURI
    playlist_uri = 'spotify:playlist:37i9dQZEVXbKXQ4mDTEBXq'

   # プレイリストから上位10曲の情報を取得
    playlist = sp.playlist(playlist_uri)
    tracks = playlist['tracks']['items'][:10]
    
    # 上位10曲の特徴量を取得してリストに変換
    track_info = []
    
    for track in tracks:
        track_name = track['track']['name']
        track_id = track['track']['id']
        features = sp.audio_features(track_id)
        track_info.append({'name': track_name, 'track_id': track_id, 'features': features})
        
    return track_info
