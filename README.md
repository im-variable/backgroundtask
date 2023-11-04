# django_celery

This is a Django project with Celery tasks for asynchronous processing.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/im-variable/backgroundtask.git
   cd backgroundtask
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Set up environment variables:

   Create a `.env` file in the project root and define the necessary variables:

   ```
   SECRET_KEY=mysecretkey
   DEBUG=True
   ```

2. Update Django settings:

   In `settings.py`, use `python-decouple` to access environment variables:

   ```python
   from decouple import config

   SECRET_KEY = config('SECRET_KEY')
   DEBUG = config('DEBUG', default=False, cast=bool)
   ```
## Running the Celery Worker

   ```bash
   celery -A backgroundtask worker -l info
   ```