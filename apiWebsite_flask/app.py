from flask import Flask, render_template
#usesd to import the current date
from datetime import date

#used to request data from API
import requests

app = Flask(__name__, static_folder= "static")

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/nasa')
def show_nasa_pic():
    #gets today's date with the date we imported at the top
    today = str(date.today())

    #gets all the data from the api depending on the day the variable today hods the data regarding the current date
    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=wjlnR0Xw9B5Sh3WEIJa9kmVd368hNMiUVIGahGPi&date='+today)

    #gets all the data from the API and sores it in a variable
    data = response.json()

    #the variable is then applied to be used in the nasa.html file
    return render_template('nasa.html', data=data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')