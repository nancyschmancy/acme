# Acme Insurance API
A simple API which creates insurance quotes, built using Django 4 and Django Rest Framework. 
## Prerequisites
To run this API, you will need Python 3.10 and virtualenv.
## Installation
1.  Unzip the Acme Insurance project. Within the project root, create a virtualenv and activate.
    ```
    python3 -m virtualenv venv
    source venv/bin/activate
    ```
2. Install requirements.
    ```
    pip install -r requirements.txt
    ```
3. Perform database migration
    ```
    python3 manage.py migrate
    ```
4. Create your login. Once prompted, enter your desired username, and password.
    ```
    python3 manage.py createsuperuser
    ```
5. You're now ready to roll! Run server:
    ```
    python3 manage.py runserver
    ```
## Basic Usage
### Authentication
Authentication is not provided for this API
### GET Requests
`GET`
## Tests
To run the test suite, run the following command:
```
python3 manage.py test
```
