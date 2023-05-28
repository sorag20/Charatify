import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_spotify_data():
    # Spotify APIのクライアント情報
    client_id = 'e9e1721fa9c44d38a8d44ab7f7418315'
    client_secret = 'ad0ccafab2d3470984903e0a0da6ef4c'

    # Spotifyクライアントを作成
    auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(auth_manager=auth_manager)

    # URI
    lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

    # URIのトップトラックを取得
    tracks = sp.artist_top_tracks(lz_uri)
    
    # トップトラックのURIをリストとして返す
    top_track_uris = [track['uri'] for track in tracks]

    return top_track_uris

    # for track in results['tracks'][:10]:
    #     print('track    : ' + track['name'])
    #     print('audio    : ' + track['preview_url'])
    #     print('cover art: ' + track['album']['images'][0]['url'])
    #     print()