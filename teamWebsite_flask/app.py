from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Kayley')
def kayley():
    return render_template('kayley.html')

@app.route('/Nana')
def nana():
    return render_template('nana.html')

@app.route('/Daniel')
def daniel():
    return render_template('daniel.html')

@app.route('/Sherry')
def sherry():
    return render_template('sherry.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')