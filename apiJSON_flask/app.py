from flask import Flask, render_template, request, json, jsonify, current_app as app, request
import os

#used to request data from API
import requests

app = Flask(__name__)
json_info = ''
movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
with open(movies_path, 'r') as raw_json:
    json_info = json.load(raw_json)


@app.route('/')
def index():
    
    return '<h1>Here is my API Data practice</h1>'

@app.route('/api/v1/album', methods=['GET'])
def album_json():
    #using with allows for opening and closing of file
    album_info = os.path.join(app.static_folder, 'data', 'album.json')
    with open(album_info, 'r') as json_data:
        json_info = json.load(json_data)
        return jsonify(json_info)

@app.route('/api/v1/movies')
def all_movies():
    return jsonify(json_info)

@app.route('/api/v1/movies/search_title', methods=['GET'])
def search_title():
    movies_path = os.path.join(app.static_folder, 'data', 'movies.json')
    with open(movies_path, 'r') as raw_json:
        json_info = json.load(raw_json)
    results = []

    if 'title' in request.args:
        #stores the results of the title the user put into the url
        title = request.args['title']
        #goes through the movies
        for movie in json_info:
            if title in movie['title']:

                results.append(movie)
                
            else:
                return render_template("movie.html", results=results)

    if len(results) < 1: 
        return "No results found"
         
    else:
        return render_template("movie.html", results=results)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0'), 
