# ReikiNoApp

## Para iniciar o projeto, use o comando abaixo:

```docker-compose up --build```

## Test App structure

- └── sql_app  
  -    ├── __init__.py  
  -    ├── crud.py  
  -    ├── database.py  
  -    ├── main.py  
  -    ├── models.py  
  -    └── schemas.py  

## Init alembic
 ``` docker-compose run --rm app alembic init alembic ```

## Check for migrations
  ``` docker-compose run --rm app alembic revision --autogenerate -m "Start app" ```

## Start migrations
  ``` docker-compose run --rm app alembic upgrade head ```