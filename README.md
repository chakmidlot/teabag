# Teabag
Send messages that will self-destruct after being read.

## Local deployment for developers ##
You need Python>=3.5.
1) Clone the repo and `cd` to the `teabag` folder
```
git clone https://github.com/chakmidlot/teabag.git
cd teabag/
```
2) Create virtual environment:
```
virtualenv -p /usr/bin/python3 --no-site-packages .tbenv
. .tbenv/bin/activate
```
3) Install dependencies:
```
pip install -r src/requirements.txt
```
4) Run it:
```
cd src
python3 webapp.py
```
Now `teabag` runs locally on port 8080.

## Production deployment to Ubuntu 16.04 ##
1) Log in as `root`
2) Install docker and docker-compose
```
apt install docker docker-compose
```
3) Clone the repo and `cd` to it
```
git clone https://github.com/chakmidlot/teabag.git
cd teabag/
```
4) Run docker-compose instructions
```
docker-compose up --build -d
```
Now `teabag` runs on port 80.
