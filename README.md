# Process of deploying Django app
## 1. Deploying using [Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html#python-django-deploy) (login: girlsleadershipstem@gmail.com)

[Install Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-virtualenv.html) in terminal in virtual environment: 

Errors in installing eb in terminal: ModuleNotFoundError: [No module named 'imp’](https://stackoverflow.com/questions/77401730/modulenotfounderror-no-module-named-imp)
<img width="698" alt="Screenshot 2024-01-29 at 6 40 23 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/1979add4-80fa-49f1-85d7-27ec11fb9dae">

[Supported platforms in elastic beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.python)

[Error: not find version that satisfies Django requirement](https://bobbyhadz.com/blog/python-could-not-find-a-version-that-satisfies-the-requirement#could-not-find-version-that-satisfies-requirement-django)


[Main error in Django EB environment](https://us-west-2.console.aws.amazon.com/elasticbeanstalk/home?region=us-west-2#/environment/dashboard?environmentId=e-up28pq6q5p&tab=health)

<img width="300" alt="Screenshot 2024-01-29 at 6 45 23 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/3cec239d-529e-4bba-b421-1ff1674b9ffb">

<img width="698" alt="Screenshot 2024-01-29 at 7 07 23 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/c843a41e-bdec-48b8-94cb-7d10ffbb90f5">

## 2. [Deploying on vercel: tutorial](https://www.youtube.com/watch?v=ZjVzHcXCeMU)
I created a new repo in GitHub for [just the backend](https://github.com/RachaelSMathew/backendSleep)

Initially couldn’t deploy successfully and got this error: 

`pip3.9 install –disable-pip-version-check –target . –upgrade -r /vercel/path0/requirements.txt`

Once I removed a majority of the packages in the requriemnts.txt 
<img width="1145" alt="Screenshot 2024-01-29 at 6 47 41 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/7494c134-6484-46c2-997b-fbc7556c6e0b">

The Vercel deployment was successful but showed this error

**Error:**

<img width="586" alt="Screenshot 2024-01-29 at 6 44 50 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/d45b14e9-4c1d-4f0e-bcde-a7d4fb02cb90">

￼
I initially tried to change to Django 2.1 so that it wouldn’t need 3.8.3, but it didn’t work because django-cors-headers, djangorestframework, djangorestframework-simplejwt rely on at least Django 3.2 version

<img width="702" alt="Screenshot 2024-01-29 at 6 53 57 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/45275333-dfa1-49bb-9217-4851f8d9f95a">

I tried to downgrade the Django to 3.2 but couldn't because 

<img width="555" alt="Screenshot 2024-01-29 at 6 52 44 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/1333e381-06d6-4814-94e0-e52267e2f5a1">

<img width="648" alt="Screenshot 2024-01-29 at 6 55 39 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/3bb033d0-69e1-4573-9742-22ec942a3644">

Tried to migrate [from SQLite to Postgresql](https://medium.com/djangotube/django-sqlite-to-postgresql-database-migration-e3c1f76711e1)

Got this error: 
<img width="569" alt="Screenshot 2024-01-29 at 6 56 47 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/b3952637-fe1c-4b36-b546-14761ac1f3ab">

Explanation of the command: 
<img width="756" alt="Screenshot 2024-01-29 at 6 57 17 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/f26a9c26-3e92-4558-a773-c9a186bed33c">

## 3. [Using Render to deploy Django App](https://www.youtube.com/watch?v=AgTr5mw4zdI) **SUCCESSFUL**: 

Note: Free tier of render expires after 90 days 

**Environment vars:**

Render: automatically uses python 3.7 (very old), so need to explicitly state the Python version in render environment vars 


`python_version: 3.10.6`

`DATABASE_URL: Internal Database URL for PostgreSQL`


External/internal db URL: allows you to connect to db from different environments 

**Packages to install for Postgres’s db in Django:**

- pycopg2-binary: python postres db adapter if you want to use Postgres’s db within Django app (Pycopg2 has issues usually so use binary)

- dj-database-url: Remotely connect to render postgres db from Django app using the external db url 
Take database url and transform into Django db parameters (name, [post, hostname) 

- Django-envioron: helps to create environment variables(keep our sensitive info private) **cannot use quotes when assigning environment var**
Configure Django app with environmental vars 
 
- gunicorn: helps bridge connection between Django app(wigs application in settings) and render web app 

Note: Gitignore .env file when uploading repo (to make it private) 

`Python manage.py` flush will truncate (delete data)
`sqlclear` will drop (delete table, thus data too)

**ERRORS:**
If you get a warning when imputing certain packages: make sure python interceptor is set up correctly

Solution: go to directory of virtual environment in terminal and do pwd to get full path and do ‘command shift p’ in visual studio code and select new python intereptor and copy in full path 

Errors I was getting when migrating with new Django external url:
```
django.db.utils.ProgrammingError: relation "authentication_customuser" does not exist
django.db.utils.ProgrammingError: relation "auth_permission" does not exist
django.db.utils.IntegrityError: null value in column "name" of relation "django_content_type" violates not-null constraint
DETAIL:  Failing row contains (13, null, admin, logentry).
```

Solution: [try resetting Django database](https://tech.raturi.in/how-reset-django-migrations)

Solution: [try faking migrations](https://stackoverflow.com/a/31324245)

<img width="674" alt="Screenshot 2024-02-06 at 6 01 06 PM" src="https://github.com/RachaelSMathew/backendSleep/assets/30049533/e453e2c9-1d9c-4d82-917c-603787b5e9bf">

Solution: `python manage.py makemigrations [EACH APP]` and then `python manage.py migrate`
