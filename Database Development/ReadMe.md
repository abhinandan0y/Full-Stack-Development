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

#### set mongodb path for data/db
```
# by default, Mongo points to that /data/db folder
sudo mkdir -p /data/db/
sudo chown `id -u` /data/db
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
```
# mongosh
Current Mongosh Log ID:	64c65c87dbe8f93639784c4c
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.10.1
Using MongoDB:		3.6.8
Using Mongosh:		1.10.1

For mongosh info see: https://docs.mongodb.com/mongodb-shell/

------
   The server generated these startup warnings when booting
   2023-07-30T17:00:04.225+0530: 
   2023-07-30T17:00:04.225+0530: ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
   2023-07-30T17:00:04.225+0530: **          See http://dochub.mongodb.org/core/prodnotes-filesystem
   2023-07-30T17:00:06.681+0530: 
   2023-07-30T17:00:06.681+0530: ** WARNING: Access control is not enabled for the database.
   2023-07-30T17:00:06.681+0530: **          Read and write access to data and configuration is unrestricted.
   2023-07-30T17:00:06.681+0530: 
   2023-07-30T17:00:06.681+0530: ** WARNING: This server is bound to localhost.
   2023-07-30T17:00:06.681+0530: **          Remote systems will be unable to connect to this server.
   2023-07-30T17:00:06.681+0530: **          Start the server with --bind_ip <address> to specify which IP
   2023-07-30T17:00:06.681+0530: **          addresses it should serve responses from, or with --bind_ip_all to
   2023-07-30T17:00:06.681+0530: **          bind to all interfaces. If this behavior is desired, start the
   2023-07-30T17:00:06.681+0530: **          server with --bind_ip 127.0.0.1 to disable this warning.
   2023-07-30T17:00:06.681+0530:

```
#### Error: mongodb Failed To Set up Listener: SocketException: Address Already in Use
```
sudo lsof -iTCP -sTCP:LISTEN -n -P
#mongod    5986      user   10u  IPv4 141244      0t0  TCP 127.0.0.1:27017 (LISTEN)
sudo kill -9 PID  #process id of mongodb 
```
