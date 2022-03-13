# flask-restplus-sqlalchemy-alembic

Create a blank migration `alembic revision -m "Migration name"`

Create a migration and detect the changes `alembic revision --autogenerate -m "Migration name"`

Run the first migration `alembic upgrade base`

Run the next migration `alembic upgrade +1`

Run all the migrations `alembic upgrade head`
