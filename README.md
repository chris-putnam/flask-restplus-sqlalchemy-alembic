# flask-restplus-sqlalchemy-alembic

Add DB models to `./database/models`

In order for the migrations to be detected add the import statement for new models to `./database/models/__init__.py`

Create a blank migration `alembic revision -m "Migration name"`

Create a migration and detect the changes `alembic revision --autogenerate -m "Migration name"`

Run the first migration `alembic upgrade base`

Run the next migration `alembic upgrade +1`

Run all the migrations `alembic upgrade head`

In order to return a model from the api you should add a DTO model to `./serializers`
