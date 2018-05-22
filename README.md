# User-Control-System
A database schema of Permission Control System to manage the users of various services that use Open Authentication.

Using SQLAlchemy ORM to work with database and Alembic to create migration files.

To create virtual environment and install dependecies run:
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```
To configure your database set DATABASE_URL environment variable, change .env file:
```
export DATABASE_URL=driver://user:password@localhost/database
```
And run:
```
source .env
```
To migrate your database run:
```
alembic upgrade head
```

To fill your database with test data run:
```
python3 -m app.inserter
```
To run test queries run:
```
python3 -m app.selections
```
