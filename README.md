
# weather_api  

## Installation 

Install `Docker`. Instructions can be found <a href="https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04">here</a>:

<br>

Create virtual env:  
  
```shell
$ python3 -m venv env
```

<br> 

Install `requirements.txt`:  
```shell
(env) $ pip3 install -r requirements.txt
```
<br>

Build `Docker` containers from images:
```shell
$ sudo docker-compose build
```
<br>

Start `Docker` containers:
```shell
$ sudo docker-compose up
```
<br>

## Available commands 

Build `Docker` containers from images:
```shell
$ sudo docker-compose build
```
<br>

Start `Docker` containers:
```shell
$ sudo docker-compose up
```
<br>

Get list of all `Docker` images:
```shell
$ docker images
```
<br>

Delete `Docker` image:
```shell
$ docker rmi <image_id>
```
<br>

Get list of all `Docker` containers:
```shell
$ docker ps -a
```
<br>

Delete `Docker` container:
```shell
$ docker rm <container_id>
```
<br>

Fill database with data:
```shell
$ make fill_crypto_db
```
 > This action requires setting ```CRYPTOCURRENCY_ACCESS_KEY```  in ```settings.py``` file

<br>

Process parsed data:
```shell
$ make process_parsed
```
> The list of other available commands is available in `Makefile`
> 

## Legacy commands

Create redis user <b>(legacy)</b>:
```
set user:1 User
```
```
set password:1 password
```
<br>

In `weather_app` directory run <b>(legacy)</b>:
```
celery -A weather_app worker --loglevel=info
```

<br>

Install PostgreSQL <b>(legacy)</b>:
```shell
$ sudo apt-get install postgresql
```
```shell
$ pip install psycopg2-binary
```

<br>

Setup and configure database <b>(legacy)</b>:
```
$ sudo -u postgres psql
```
```sql
Postgres=# CREATE DATABASE weather_db;
```
```sql
Postgres=# CREATE USER admin WITH PASSWORD ‘1111‘;
```
```sql
Postgres=# ALTER ROLE admin SET client_encoding TO ‘utf8’;
```
```sql
Postgres=# ALTER ROLE admin SET default_transaction_isolation TO ‘read committed’;
```
```sql
Postgres=# ALTER ROLE admin SET timezone TO ‘UTC’;
```
```sql
Postgres=# GRANT ALL PRIVILEGES ON DATABASE weather_db TO admin;
```

<br>

Exit SQL console:
```sql
Postgres=# \q
```
<br>
