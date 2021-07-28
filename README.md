
# weather_api  

## Installation 

Create virtual env:  
  
```shell
$ python3 -m venv env
```

<br> 
  
Install requirements:  
```shell
$ pip3 install -r requirements.txt
```
<br> 

## Weather API  

Create redis user:
```
set user:1 User
```
```
set password:1 password
```

<br>

In weather_app run:
```
celery -A weather_app worker --loglevel=info
```

<br>

## Currency API

Install PostgreSQL:
```shell
$ sudo apt-get install postgresql
```
```shell
$ pip install psycopg2-binary
```

<br>

Setup and configure database:
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

Fill database with data:
```shell
$ python3 manage.py fill_crypto_db
```

 > This action requires setting ```CRYPTOCURRENCY_ACCESS_KEY```  in ```settings.py``` file

Process parsed data:
```shell
$ python3 manage.py process_parsed
```
