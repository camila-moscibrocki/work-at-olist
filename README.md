# Books Database API project

Database created with Django as framework, Python API rest and heroku deploy

## Prerequisites

This project runs in python 3.6 and Django 2.2.8,  the controls listed below were used in windows 10 and Pycharm terminal.

It also have the requirements bellow:  
dj-database-url==0.5.0  
dj-static==0.0.6  
Django==2.2.8  
django-filter==2.2.0  
djangorestframework==3.11.0  
python-decouple==3.3  
pytz==2019.3  
sqlparse==0.3.0  
static3==0.7.0  

Or you can install it:
```
pip install -r requirements.txt
```

### Project Link
https://books-database00.herokuapp.com/

### Admin credentials
User: Admin  
Password: Admin

## Installing

Virtual environment:

```
virtualenv venv
```

To activate:

```
. venv/Scripts/activate
```

## Database

This project uses db.sqlite3 database for storage, any changes must be migrated to the base as follows:
```
python manage.py makemigrations
python manage.py migrate
```

## Tests

You can manually run tests using the file "tests" located in books and authors directory or by using:
```
$ python manage.py test
```
