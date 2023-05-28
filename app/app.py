from flask import Flask,render_template
from api import get_top10_tracks

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def data():
    top10_tracks = get_top10_tracks()
    return render_template('data.html',top10_tracks=top10_tracks)

if __name__ == '__main__':
    app.run(debug=True)