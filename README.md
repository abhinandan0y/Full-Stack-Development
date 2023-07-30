# Full-Stack-Development 
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fabhinandan0y%2FFull-Stack-Development%2Ftree%2Fmain&count_bg=%2379C83D&title_bg=%23555555&icon=jabber.svg&icon_color=%23FFFFFF&title=hits&edge_flat=false"/></a>
<a href="https://abhinandan0y-Full-Stack-Development-xpx37u3zfpq.ws-us101.gitpod.io/"><img src="https://img.shields.io/badge/Gitpod-ready--to--code-FFB45B?logo=gitpod url=https://gitpod.io/#https://github.com/abhinandan0y/Full-Stack-Development"/></a>
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Technologies used : 
```
Database: MongoDb
Backend: Flask
Frontend: HTML CSS JavaScript
```
### check and kill if any server running in background
```
sudo lsof -iTCP -sTCP:LISTEN -n -P
##sudo kill -9 pid
```
#### MongoDb
```
mongodb ##port 27017
### use newdatabase(name of new database) to create a new database
use test
### insertOne to insert one value into database.
db.test.insertOne({x:1})
### to check the new database has been created.
show dbs 
### import data from another termonal.
Using mongoimport 
mongoimport --db test --type tsv --headerline --ignoreBlanks --file /home/abhinandan/MongoDB/data/CharacterizedGenes.csv
### to present all databases
show dbs 
### show tables/collections
show tables
```
#### Flask
```
export FLASK_APP=app
export FLASK_ENV=development
flask run ###port 5000
```


https://raw.githack.com/abhinandan0y/Full-Stack-Development/main/index.html


**#Knowlegde is FREE but Solution is Your's🤘🏻**

**Keep on Learning and Executing...🏃🏻** contact@:bioinformaticsfuture@gmail.com
<div style="width: 100%;">
  <img src="https://www.bioinformaticsfuture.com/images/bioinformatics_lab.png" style="width: 100%;" alt="bioinformatics_lab.png">
</div>



