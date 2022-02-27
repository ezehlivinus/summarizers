# summarizers
This is a demo - file database used

# Usage
- clone the repo and cd into it
- create a `.env` and check sample content from `.env.example`
## Epic
  - create or activate an environment
  - install dependencies: `pip install -r requirements.txt`
  - make migrations: `python manage.py makemigrations`
  - migrate: `python manage.py migrate`
  - run server: `python manage.py runserver`
  - app running: `http://localhost:8000/`
## Docker
You should already have docker install and setup on your machine.
  - Build a docker image of the app: `docker build --tag summarizers .` tag name is 'summarizers', it can be anything you want
  - Run the docker image as a container: `docker run --publish 8000:8000 summarizers`
  - app running: `http://localhost:8000/`

# App Documentation
Access the app docs:
- `http://localhost:8000/docs/`


