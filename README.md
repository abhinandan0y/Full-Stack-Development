# Full-Stack-Development 
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fabhinandan0y%2FFull-Stack-Development&count_bg=%2379C83D&title_bg=%23555555&icon=jabber.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
<a href="https://abhinandan0y-Full-Stack-Development-xpx37u3zfpq.ws-us101.gitpod.io/"><img src="https://img.shields.io/badge/Gitpod-ready--to--code-FFB45B?logo=gitpod url=https://gitpod.io/#https://github.com/abhinandan0y/Full-Stack-Development"/></a>
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment notes on how to deploy the project on a live system.<br>
https://raw.githack.com/abhinandan0y/Full-Stack-Development/main/index.html
<br><br>
I used **Mongodb** as database to store test data and **Flask** to get data from database using **pymongo**. And finally incorporated data through flask in **html** rendered through **jinja** for full stack development alongwith **jQuery** to use **JavaScript** on the website to make it more interactive and attractive.


### Technologies used : 
```
Database: MongoDb
Backend: Flask
Frontend: HTML CSS jQuery JavaScript
```
### Install MongoDB 
```
#From a terminal, install gnupg and curl if they are not already available:
sudo apt-get install gnupg curl
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor
#Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
#UPDATE for installing mongodb
sudo apt-get update
#Install the MongoDB packages.
sudo apt-get install -y mongodb-org
```

##### set mongodb path for data/db
```
# by default, Mongo points to that /data/db folder
sudo mkdir -p /data/db/
sudo chown `id -u` /data/db
```
##### Start mongodb
```
sudo systemctl start mongod
sudo systemctl status mongod
● mongod.service - MongoDB Database Server
     Loaded: loaded (/lib/systemd/system/mongod.service; enabled; preset: enabled)
     Active: active (running) since Fri 2023-07-14 17:18:19 IST; 6s ago
       Docs: https://docs.mongodb.org/manual
   Main PID: 195647 (mongod)
     Memory: 66.8M
        CPU: 499ms
     CGroup: /system.slice/mongod.service
             └─195647 /usr/bin/mongod --config /etc/mongod.conf

Jul 14 17:18:19 user systemd[1]: Started mongod.service - MongoDB Database Server.
Jul 14 17:18:19 user mongod[195647]: {"t":{"$date":"2023-07-14T11:48:19.722Z"},"s":"I",  "c":"CONTROL",  "id":7484500, "ctx":"-","msg":"Environment variable MONGODB_CONFIG_OVERRIDE_NOFORK == 1, overriding \"processManagement.fork\" to false"}
...
```
##### Error: mongodb Failed To Set up Listener: SocketException: Address Already in Use
```
### check and kill if any server running in background
sudo lsof -iTCP -sTCP:LISTEN -n -P
#mongod    5986      user   10u  IPv4 141244      0t0  TCP 127.0.0.1:27017 (LISTEN)
sudo kill -9 PID  #process id of mongodb 
```
#### MongoDb
```
mongodb ##port 27017
### use newdatabase(name of new database) to create a new database
use BSL
switched to db BSL
### to check the new database has been created.
show dbs
```
```
### import data from another termonal.
Using mongoimport
#if you don't mention collections name it will take from filename
mongoimport --db BSL --type tsv --headerline --ignoreBlanks --file /home/abhinandan/MongoDB/data/clusters.csv
```
```
### to present all databases
show dbs 
### show tables/collections
##############################################
BSL> show tables
barcode_clusters
clusters
BSL> db.clusters.find()
[
  {
    _id: ObjectId('6853b971a7fb7d3da6e5a6ef'),
    barcode: 'barcode73',
    count: 44
  },
###############################################
BSL> db.clusters.find().count()
13
```
#### pymongo
```
pip install pymongo
```
#### Flask
```
pip install flask
#folder structure #export should be done inside main(app) folder
app/
|
└── app.py
└── templates
   └── index.html
export FLASK_APP=app
export FLASK_ENV=development
flask run ###port 5000
```


**#Knowlegde is FREE but Solution is Your's🤘🏻**

**Keep on Learning and Executing...🏃🏻** contact@:bioinformaticsfuture@gmail.com
<div style="width: 100%;">
  <img src="https://www.bioinformaticsfuture.com/images/bioinformatics_lab.png" style="width: 100%;" alt="bioinformatics_lab.png">
</div>



