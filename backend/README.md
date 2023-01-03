# Backend Documentation

This app consists a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py`. To define your endpoints and can reference `.database/models.py` for DB and SQLAlchemy setup. These are the files you'd primarily be focusing on in the backend:

1. `backend/flaskapp/__init__.py`
2. `backend/database/models.py`

How to set up on your local machine and all available endpoints are documented below. More endpoints will be created as the project coninues.

### Endpoints 

Home(def home), Methods = GET
This is the endpoint of the official homepage. Returns a message telling the title and version of the project


### Testing 

Every endpoint is required to also have a test function in the test.py file to ensure the appropriate return values and format


### Setting up

To set up, you must have python installed, find guides on that [here](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python). Clone the repo by navigating to your chosen directory for the project in your git bash terminal and running the following command:

`git clone https://github.com/JhimmieC137/conference-wesite.git`


Create a virtual environment and activate using any of the commands below in your terminal

`python -m venv <virtual environment name>` --> `cd <virtual environment name>` --> `Scripts\activate`

or

For Linux:
`virtualenv <virtual environment name>` --> `source <virtual environment name>/bin/activate` 



In the backend directory, run the command `pip install -r requirements.txt` to install all dependencies in the requirements text file


### Running the app

To run the flask app, in the backend directory, set the flask app to your environment and to development mode. Use the following commands in your terminal

Windows CMD:
```
set FLASK_APP=flaskapp
set FLASK_DEBUG=True
```

Windows Powershell:
```
$env:FLASK_APP=flaskapp
$env:FLASK_DEBUG=True
```

Unix Bash(Linux, Mac, etc.):
```
export FLASK_APP=flaskapp
export FLASK_DEBUG=True
```

and then `flask run`


Confirm it runs by navigating to project homepage on your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000](http://localhost:5000) 

**Now you're ready!**
