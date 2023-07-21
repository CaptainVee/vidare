
# Vidare 
Extract text from PDF or Powerpoint documents

## Want to use this project?

1. Fork/Clone

   ```sh
   $ git clone https://github.com/CaptainVee/vidare.git
   ```

1. Cd into vidare
   ```sh
   $ cd vidare
   ```
1. Create and activate a virtual environment:

   ```sh
   $ python3 -m venv venv && source venv/bin/activate
   ```

1. Install the dependencies:

   ```sh
   (venv)$ pip install -r requirements.txt
   ```

1. Apply the migrations and run the Django development server:

   ```sh
   (venv)$ python manage.py makemigrations
   (venv)$ python manage.py migrate
   (venv)$ python manage.py runserver
   ```

1. Test at [http://localhost:8000/](http://localhost:8000/)

upload a document with the form at the top right corner and submit to get the extracted text.

