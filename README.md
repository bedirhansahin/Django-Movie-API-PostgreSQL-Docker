## WELCOME MY MOVIE_API

### This API app is being built with django, django rest framework, and postgresql on docker

### Follow the steps, below to run the app:

```
git clone https://github.com/bedirhansahin/Django-Movie-API-PostgreSQL-Docker.git
```
```
cd Django-Movie-API-PostgreSQL-Docker
```
```
docker-compose up --build
```
If you do not want to empty database, after this step, open a new terminal and run: 
```
docker-compose run --rm app sh -c "python3 sql_insert.py"
```
This command going to create some datas and an admin user that username is **admin** and password is **123456**