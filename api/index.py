from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/contactus')
def contactus ():
    return '<h1> Anish </h1>'

@app.route('/twiliodata', methods=['POST'])
def twiliodata ():
    print ("message received")
    return '<h1> Anish </h1>'
