# django_celery

This is a Django project with Celery tasks for asynchronous processing.

# Installation
Clone this repository:
git clone https://github.com/im-variable/backgroundtask.git
cd backgroundtask

# Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
Install project dependencies:

pip install -r requirements.txt

# Configuration
Set up environment variables:

Create a .env file in the project root and define the necessary variables:
SECRET_KEY=mysecretkey
DEBUG=True

Update Django settings:
In settings.py, use python-decouple to access environment variables:
from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)


# Running the Celery Worker
Start the Celery worker in a separate terminal window:

celery -A project_name worker -l info