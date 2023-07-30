### Install MongoDB 
```
#From a terminal, install gnupg and curl if they are not already available:
sudo apt-get install gnupg curl
curl -fsSL https://pgp.mongodb.com/server-6.0.asc | \
   sudo gpg -o /usr/share/keyrings/mongodb-server-6.0.gpg \
   --dearmor
#Create a list file for MongoDB
echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-6.0.gpg ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
#Install the MongoDB packages.
sudo apt-get install -y mongodb-org
```
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

Jul 14 17:18:19 Progenesis systemd[1]: Started mongod.service - MongoDB Database Server.
Jul 14 17:18:19 Progenesis mongod[195647]: {"t":{"$date":"2023-07-14T11:48:19.722Z"},"s":"I",  "c":"CONTROL",  "id":7484500, "ctx":"-","msg":"Environment variable MONGODB_CONFIG_OVERRIDE_NOFORK == 1, overriding \"processManagement.fork\" to false"}
...

```
#### Begin using MongoDB
'''
mongosh






```
