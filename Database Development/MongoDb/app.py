from flask import Flask
from pymongo import MongoClient
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)

client = MongoClient('localhost', 27017)

db = client.BjuDb
CharacterizedGenes = db.CharacterizedGenes


'''
@app.route('/', methods=('GET', 'POST'))
def index():
    return render_template('index.html')
'''
@app.route('/', methods=('GET', 'POST'))
def index():
 
    all_CharacterizedGenes = CharacterizedGenes.find()
    return render_template('index.html', CharacterizedGenes=all_CharacterizedGenes)
    

