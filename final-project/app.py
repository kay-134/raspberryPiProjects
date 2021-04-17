from flask import Flask, redirect,render_template, url_for, request
from sense_emu import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
import sqlite3
import sys
sense = SenseHat()
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
                           

@app.route('/success', methods=['GET','POST'])
def success():
   #get posted from data  using names assigned in HTML
   message = request.form['message']
   name = request.form['name']
    
   #generate string to display on Sense HAT
   display  = message  + " Sincerely" + name

   #connect to database and insert message and name 
   conn = sqlite3.connect('./static/data/senseDisplay.db')
   curs = conn.cursor()
   curse.execute("INSERT INTO messages (name, message) VALUES((?),(?))", (name, message))

   #reset sensehat
   #sense.clear(255,255,255)
  
   #display message on Sense HAT
   #sense.show_message(message)
   return render_template('success.html', name = name, message = message)

@app.route('/all')
def all():
    #connect to DB
   conn = sqlite3.connect('./static/data/senseDisplay.db')
   curs = conn.cursor()
   messages = []
   rows = curs.execute("SELECT * from messages")
   for row in rows:
      message = {'name': row[0], 'message':row[1]}
      messages.append(message)
   conn.close()
   return render_template('all.html', name = name, messages = messages)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
