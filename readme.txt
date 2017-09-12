
Read this file and execute

This is a template project to display django knowledge

Use virtualenv for django projects always. \
Install virtualenv wrapper to keep track of them




django-admin.py startproject directory

python manage.py startapp www

python manage.py runserver

# migrate data to sqlite3.db
python manage.py makemigrations
python manage.py migrate

# create for admin login
python manage.py createsuperuser

#load preliminary data from .json file in fixtures

use gunicorn for production deployment
create Procfile for this gunicorn


Hosted on Heroku





Always the .gitignore file, so everything in your computer does not load up in GITHUB.


{{ Commands for virtualenv setup:

Add gitignore file

mkvirtualenv --python=python3 superlists

workon superlists

pip install "django<1.12" "selenium<4"



deactivate


pip freeze



lsvirtualenv -b


Atom packages
youtube
alexander kallaway }}
