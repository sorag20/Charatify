from flask import Flask,render_template,request
from api import get_top10_tracks
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
    #比較項目をcharacterに入れる
    for item in character.keys():
        character[item]=request.form[item]
        
    top10_tracks = get_top10_tracks()
    return render_template('data.html',top10_tracks=top10_tracks,recommended_song_params=search_song(top10_tracks,character))

if __name__ == '__main__':
    app.run(debug=True)