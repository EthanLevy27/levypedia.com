from fileinput import filename
from flask import Flask, render_template, url_for, request
import json

app = Flask(__name__)

@app.route("/songwrite/<song>", methods=["POST", "PUT"])
def songwrite(song=None):
    file = open("songs.json", "r")
    list = json.load(file)
    print(list)
    list.append(song)
    file = open("songs.json", "w")
    json.dump(list, file)
    file.close()
    return 200

@app.route("/songread", methods=["GET"])
def songread():
    file = open("songs.json", "r")
    list = json.load(file)
    return 200

@app.route("/backpacking_photos")
def backpacking_photos():
    return render_template('backpacking_photos.html')

@app.route("/")
def home():
    url_for('static', filename='playlist_store.js')
    url_for('static', filename='playlist.js')
    url_for('static', filename='style.css')
    url_for('static', filename='levypedia.css')
    url_for('static', filename='Profile-Picture.jpeg')
    url_for('static', filename='backpacking_photos.html')
    return render_template('index.html')