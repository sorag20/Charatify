from api import get_top10_tracks
import math

def search_song(get_top10_tracks, character):
    
    #名前と曲のリンクを返す
    Recommended_song_params={'name':'','track_href':''}
    max_similarity=0
    
    #取得した曲と類似度を計算（ユークリッド距離）
    for song in get_top10_tracks:
        squares = [(float(song['features'][0][key]) - float(value)) ** 2 for key,value in character.items()]
        sum_of_sqrt = math.sqrt(sum(squares))
        similarity=1/(1 + sum_of_sqrt)
        #類似度が一番大きい曲を返す
        if similarity>max_similarity:
            Recommended_song_params['name']=song['name']
            Recommended_song_params['track_href']=song['features'][0]['track_href']
            max_similarity=max(max_similarity,1/(1 + sum_of_sqrt))
            
    return  Recommended_song_params
