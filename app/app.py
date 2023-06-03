from flask import Flask,render_template,request

from api import get_tracks_features

from search import search_song

app=Flask(__name__,static_folder=None)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data",methods=["GET","POST"])
def data():
    #比較項目のdict
    character={'acousticness':0,'danceability':0,'energy':0,
               'liveness':0,'tempo':0,'valence':0}

    character_popularity = {'popularity':0}
    #比較項目をcharacterに入れる
    for item in character.keys():
        character[item]=request.form[item]
    
    #プレイリストの取得
    target_uri_lists = []
    target_uri_lists.append('spotify:playlist:3gBtD7jFYrZBe3KdHTZZ5g') 
    target_uri_lists.append('spotify:playlist:44LUPVEtZXgsrQsuhZ80H2') 
    target_uri_lists.append('spotify:playlist:1evv2TiAXBAxPNCs1UIiR0') 
    target_uri_lists.append('spotify:playlist:0vFfiMBEf7M4Y0thiVVaH8') 
    target_uri_lists.append('spotify:playlist:2nZdwEso65CYx84J0h2urc') 
    target_uri_lists.append('spotify:playlist:3ImtYjNjsgN3NtfGP5LFKN') 
    
    #曲の特徴量のリストを確保するためのリスト
    trackslist_with_features = []
    
    for i in range(len(target_uri_lists)):
        tracks_with_features = get_tracks_features(target_uri_lists[i])
        trackslist_with_features.append(tracks_with_features)
    
    return render_template('data.html',trackslist_with_features=trackslist_with_features,recommended_song_params=search_song(trackslist_with_features,character,character_popularity))

if __name__ == '__main__':
    app.run(debug=True)