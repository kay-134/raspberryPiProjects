from flask import Flask, redirect,render_template, url_for, request
from sense_emu import SenseHat   #import the SenseHat object from the sense_hat library
from time import sleep
sense = SenseHat()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
                           

@app.route('/success', methods=['GET','POST'])
def success():
   message = request.form['message']
   sense.show_message(message)
   return render_template('success.html', message = message)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.4')