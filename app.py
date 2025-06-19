from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
client = MongoClient('localhost', 27017)
db = client.BSL
clusters = db.clusters

@app.route('/', methods=['GET', 'POST'])
def index():
    all_clusters = list(clusters.find())  # <-- convert cursor to list
    print(all_clusters)  # <-- Python 3 print
    return render_template('index.html', clusters=all_clusters)

if __name__ == '__main__':
    app.run(debug=True)

