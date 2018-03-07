Simple Todo Django App

How to setup the app

Install pipenv with 
  pip install pipenv
  cd backend/
  pipenv shell
the run 
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
now the api can be accessed with
127.0.0.1:8000/api/todo

127.0.0.1:8000/api/todo/<id>
