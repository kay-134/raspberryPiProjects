from flask import Flask, render_template, request, json, jsonify, current_app as app
import os

#used to request data from API
import requests

app = Flask(__name__, static_folder= "static")

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/api/v1/album', methods=['GET'])
def album_json():
    album_info = os.path.join(app.static_folder, 'data', 'album.json')
    with open(album_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')