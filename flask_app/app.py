import datetime
from flask import Flask, render_template, request, url_for, jsonify
from pymongo import MongoClient


app = Flask(__name__)

host = 'localhost'
port = 27017
client = MongoClient(host, port)
db = client['historical_wx_data']


@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')


@app.route('/helpful-links/')
def helpfullinks():
    return render_template('helpful-links.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=30006, debug=True)
