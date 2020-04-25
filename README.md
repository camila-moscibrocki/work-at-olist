# Books Database API project

Database created with Django as framework, Django REST for Web API rest and heroku deployment

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

## Project details

### Authors output data

You can also check it at https://books-database00.herokuapp.com/authors/
```
[
    {
        "id": 1,
        "name": "Luiz Henrique Hugria"
    },
    {
        "id": 2,
        "name": "Mauricio Samy Silva"
    },
    {
        "id": 3,
        "name": "Pablo Dall Oglio"
    },
    {
        "id": 4,
        "name": "Yehuda Katz"
    },
    {
        "id": 5,
        "name": "Bear Bibeault"
    },
    {
        "id": 6,
        "name": "Maurice Petyt"
    },
    {
        "id": 7,
        "name": "Harry Percival"
    }
]
```

### Books output data

You can also check it at https://books-database00.herokuapp.com/Books/
```
[
    {
        "id": 1,
        "title": "TDD com Python",
        "edition": 2.0,
        "publication_year": 2017,
        "author": [
            {
                "id": 7,
                "name": "Harry Percival"
            }
        ]
    },
    {
        "id": 2,
        "title": "Segurança Operacional de Trens de Carga",
        "edition": 2.0,
        "publication_year": 2018,
        "author": [
            {
                "id": 1,
                "name": "Luiz Henrique Hugria"
            }
        ]
    },
    {
        "id": 3,
        "title": "JQuery em ação",
        "edition": 2.0,
        "publication_year": 2012,
        "author": [
            {
                "id": 4,
                "name": "Yehuda Katz"
            },
            {
                "id": 5,
                "name": "Bear Bibeault"
            }
        ]
    },
    {
        "id": 4,
        "title": "PHP",
        "edition": 3.0,
        "publication_year": 2015,
        "author": [
            {
                "id": 3,
                "name": "Pablo Dall Oglio"
            }
        ]
    },
    {
        "id": 5,
        "title": "HTML5",
        "edition": 2.0,
        "publication_year": 2011,
        "author": [
            {
                "id": 2,
                "name": "Mauricio Samy Silva"
            }
        ]
    }
]
```

## This project was built With

* [Heroku](http://www.heroku.com) - The platform as a service (PaaS) used for deployment
* [Django](https://www.djangoproject.com/) - Framework for web devlopment
* [Django-Rest](https://www.django-rest-framework.org/) - for building Web API
