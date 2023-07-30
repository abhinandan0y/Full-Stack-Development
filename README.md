# Full-Stack-Development

# check and kill if any server running in background
sudo lsof -iTCP -sTCP:LISTEN -n -P
##sudo kill -9 pid
# ################################  MongoDb  ####################################
mongodb ##port 27017
# use newdatabase(name of new database) to create a new database
use test
# insertOne to insert one value into database.
db.test.insertOne({x:1})
# to check the new database has been created.
show dbs 
# import data from another termonal.
Using mongoimport 
mongoimport --db test --type tsv --headerline --ignoreBlanks --file /home/abhinandan/MongoDB/data/CharacterizedGenes.csv
# to present all databases
show dbs 
# show tables/collections
show tables
# ################################  Flask  ######################################
export FLASK_APP=app
export FLASK_ENV=development
flask run ##port 5000





https://raw.githack.com/abhinandan0y/Full-Stack-Development/main/index.html
