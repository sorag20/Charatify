from flask import Flask,render_template
from api import get_spotify_data

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def data():
    spotify_data = get_spotify_data()
    return render_template('data.html', spotify_data=spotify_data)

if __name__ == '__main__':
    app.run(debug=True)