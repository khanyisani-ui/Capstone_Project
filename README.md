# Event Management API

## Setup Instructions

1. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`

Install the requirements:
pip install django djangorestframework

Run migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver


Endpoints
/api/users/ - List and create users
/api/users/<int:id>/ - Retrieve, update, and delete a user
/api/events/ - List and create events
/api/events/<int:id>/ - Retrieve, update, and delete an event
/api/events/upcoming/ - List upcoming events


Deployment
For deployment, you can use either Heroku or PythonAnywhere. Here is a brief overview for both:

Deploying to Heroku:
Install Heroku CLI:
curl https://cli-assets.heroku.com/install.sh | sh

Create a Procfile:
web: gunicorn event_management.wsgi

Create requirements.txt:
pip freeze > requirements.txt

Create a Heroku App and Deploy:
heroku create your-app-name
git push heroku master
heroku run python manage.py migrate
Deploying to PythonAnywhere:
Sign Up and Log In to PythonAnywhere.

Create a New Web App:

Select "Manual Configuration".
Choose Python 3.x.
Configure the Web App:

Set the source code directory.
Point to event_management.wsgi for the WSGI configuration file.

Set Up a Virtual Environment on PythonAnywhere:
mkvirtualenv --python=python3.8 your-venv-name
pip install -r requirements.txt

Add Environment Variables and Run Migrations:
python manage.py migrate
