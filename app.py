from flask import Flask
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.test
Test = db.Test


'''
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
'''
@app.route('/', methods=('GET', 'POST'))
def index():
 
    all-data_Test = Test.find()
    return render_template('index.html', Test=all-data_Test)
    

