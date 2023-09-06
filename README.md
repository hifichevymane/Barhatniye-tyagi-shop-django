# Barhatniye tyagi shop Django

### This is an e-commerce clothes shop built on Django using PostgreSQL

## Requirements:
1. Python>=3.11
2. PostgreSQL

## Installation:
1. Create a virtual environment:
```
python -m venv venv
```
2. Activate the virtual environment:

> *Windows*:
```
venv\Scripts\activate
```
> *Linux and MacOS:*
```
source venv/bin/activate
```

3. Install all dependencies:
```
pip install -r requirements.txt
```

4. Create Postgres db for a project

6. Create **.env** file in "barhatniye_tyagi/barhatniye_tyagi/" directory and edit it like this:
```
NAME=(dbname)
USER=(dbuser)
PASSWORD=(dbpassword)
HOST=localhost
PORT=5432
```

6. Run the project:
```
python manage.py runserver
```
