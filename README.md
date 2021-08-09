
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

Delete all stopped `Docker` containers:
```shell
$ docker container prune
```
<br>

Delete all unused `Docker` images:
```shell
$ docker image prune -a
```
<br>

Delete all dangling `Docker` images:
```shell
$ docker image prune
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

## GraphQL

`GraphQL` module can be accessed by going to `/graphql` link.

<br>

### Writing queries

For example, to get all `shawarmas`, we can use this query:
```graphql
query get_shawarmas {
  allShawarmas{
    edges {
      node {
        id
        name
        weight
        price
        ingredients {
          id
          name
        }
      }
    }
  }
}

```

The expected result is:
```json
{
  "data": {
    "allShawarmas": {
      "edges": [
        {
          "node": {
            "id": "U2hhd2FybWFOb2RlOjE=",
            "name": "Шаурма восточная с курицей",
            "weight": 335,
            "price": 93,
            "ingredients": [
              {
                "id": "1",
                "name": "огурец соленый"
              },
              {
                "id": "2",
                "name": "лаваш арабский"
              },
              {
                "id": "3",
                "name": "мясо куриное"
              },
              {
                "id": "4",
                "name": "чесночный соус"
              },
              {
                "id": "5",
                "name": "зелень"
              }
            ]
          }
        },
        ...
```
<br>

We can filter our result set. For example, to get all `shawarmas`, whose name contain a `<string>`, we can use this query:
```graphql
query get_shawarmas {
  allShawarmas(name_Icontains: "<string>") {
    edges {
      node {
        id
        name
        weight
        price
        ingredients {
          id
          name
        }
      }
    }
  }
}
```
<br>

To get <i>specific</i> `shawarma`, we can use this query:
```graphql
query get_shawarmas {
  shawarma(id: "U2hhd2FybWFOb2RlOjE="){
    id
    name
    weight
    price
  }
}
```
<br>

Here is the list of all available lookup expressions and examples:
```graphql
(name: "курица")            # Exact search
(name_Icontains: "курица")  # Contains
(weight_Lt: 400)            # Less than
(price_Gt: 100)             # Greater than
```


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
```shell
$ celery -A weather_app worker --loglevel=info
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
```shell
$ sudo -u postgres psql
```
```sql
Postgres=# CREATE DATABASE weather_db;
```
```sql
Postgres=# CREATE USER admin WITH PASSWORD '1111';
```
```sql
Postgres=# ALTER ROLE admin SET client_encoding TO 'utf8';
```
```sql
Postgres=# ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
```
```sql
Postgres=# ALTER ROLE admin SET timezone TO 'UTC';
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
