from api import get_tracks_features
import math

def search_song(tracklist_with_features, character, character_popularity):
    
    #名前と曲のリンクを返す
    Recommended_song_params={'name':'' ,'artist':'', 'track_href':''}
    max_similarity=0
    
    #取得した曲と類似度を計算（ユークリッド距離）
    for trackitems in tracklist_with_features:
        for song in trackitems:
            squares = [(float(song['track_features'][key]) - float(value)) ** 2 for key,value in character.items()]
            squares_popularity = [int(song['popularity'] - value) ** 2 for value in character_popularity.values()]
            sum_of_sqrt = math.sqrt(sum(squares) + sum(squares_popularity))
            similarity=1/(1 + sum_of_sqrt)
            #類似度が一番大きい曲を返す
            if similarity>max_similarity:
                Recommended_song_params['name']=song['track_name']
                Recommended_song_params['artist']=song['artist']
                Recommended_song_params['track_href']=song['track_features']['track_href']
                max_similarity=max(max_similarity,1/(1 + sum_of_sqrt))
            
    return  Recommended_song_params