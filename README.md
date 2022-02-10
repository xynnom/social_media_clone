# ARCU Backend

A type of social media API clone that has users, comments, posts, and messaging.


You can find the API documentation here: http://loclahost:8800/docs


Deployment of ARCU API server

killing all gunicorn processes for arcu
```sh
for pid in $(ps -ef | grep "uvicorn.workers.UvicornWorker" | awk '{print $2}'); do kill -9 $pid; done
```

**Running fastAPI on Dev:**
```sh
uvicorn main:app --reload --host 0.0.0.0 --port 8800
```
**Running fastAPI using gunicorn on Prod:**
```sh
cd social_media_clone/src
gunicorn --daemon --log-file <log_file> -w 1 -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8800
```


**Using Docker-Compose**

```sh
docker-compose -f docker-compose.yml up --build
```


**DB Migration**

The app uses `alembic` for db migrations. The documentation of alembic can be found here: https://alembic.sqlalchemy.org/en/latest/autogenerate.html.

If fresh pull from repo and a fresh psql db.
```sh
cd social_media_clone/src
alembic upgrade head
```

**If there are changes to the models, you need to migrate the changes to the db.**
1. Add a `revision` based on the changes:
```sh
cd social_media_clone/src
alembic revision --autogenerate -m "<comment/message for the revision>"
```
2. Check the `social_media_clone/src/db-migration/version/` if a new version file is added.
If there are revision file added:
```sh
cd social_media_clone/src
alembic upgrade head
```
