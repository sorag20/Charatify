import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify APIのクライアント情報
# client_id = 'e9e1721fa9c44d38a8d44ab7f7418315'
# client_secret = 'ad0ccafab2d3470984903e0a0da6ef4c'
client_id = '44a92c7fdc2b4c46ba0592c5bd1fc4fb'
client_secret = '22fd6a34d57842348acfa41f10d6f6ae'

# Spotifyクライアントを作成
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# 指定されたプレイリストのurlにある曲の特徴量を取得する
def get_tracks_features(url):
    
    track_info = []
    
    tracks_with_features = []
    
    # プレイリストの曲をページングして取得
    offset = 0
    limit = 50
    while True:
        response = sp.playlist_items(url, offset=offset, limit=limit)
        tracks = response['items']
        for track in tracks:
            track_info = track['track']
            track_uri = track_info['uri']

            # 曲の詳細情報を取得
            track_details = sp.track(track_uri)

            # 曲名とアーティスト名を取得
            track_name = track_details['name']
            artists = [artist['name'] for artist in track_details['artists']]

            # 特徴量を取得
            track_features = sp.audio_features(track_uri)[0]

            # 特徴量を辞書としてリストに追加
            track_data = {
                'track_name': track_name,
                'artist': artists,
                'track_features': track_features,
                'popularity': track_details['popularity']
            }
            tracks_with_features.append(track_data)

        # 次のページがない場合は終了
        if not response['next']:
            break

        # 次のページのオフセットを更新
        offset += limit

    return tracks_with_features