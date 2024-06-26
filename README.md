# REST API

Basic example of REST API to consume and return geospatial data.

# How to build

## Docker

### Requirements

#### Docker env

[Follow the instructions here to install Docker on Win](https://docs.docker.com/desktop/install/windows-install/)

### Step-by-step installation

Download the app code from GitHub:

```git clone https://github.com/janclod/REST-example.git``` 

Move to the repository directory (`cd ./REST-example`) and spin up Docker container:

```docker-compose up -d --build```

Perform first migration:

```docker-compose exec web python manage.py migrate```

Load the data into the DB:

```docker-compose exec web python load.py```

Enjoy visiting the freshly installed app in the web browser by visiting:

```http://127.0.0.1:8000/municipalities/?format=json```

You can also filter municipalities using a bounding box:

```http://127.0.0.1:8000/municipalities/?in_bbox=4,6,50,60&format=json```

## Local Python environment

### Requirements

#### Python env

You require Python (with venv) to install this project.

On Ubuntu:

```sudo apt install python3 python-is-python3 python3.10-venv python3-pip```

See: [Python guide](https://docs.python-guide.org/starting/install3/linux/)

#### Database backend

Need to have a running instance of Postgresql.

The Postgresql instance must be reachable from the location where the app is running on standard port (`5432`).

The Postgresql instance must have a standard username `postgres` (password `postgres`).

The Postgresql instance must contain a DB named `db` with postgis extension.

The `postgres` username must own the `db` DB and have create/read/write rights.

See:  [Django guide](https://docs.djangoproject.com/en/5.0/ref/contrib/gis/install/postgis/)

#### Python packages

- django
- rest_framework
- rest_framework_gis
- requests
- psycopg2

### Step-by-step installation (for developers)

Download the app code from GitHub:

```git clone https://github.com/janclod/REST-example.git``` 

Move to the repository directory (`cd ./REST-example`) and set up virtual env:

```
python -m venv .
source ./bin/activate
```

Install deps:

```python -m pip install -r requirements.txt```

Run the first migration to create the right tables:

```python manage.py migrate```

Launch the app:

```python manage.py runserver```

Load the data (in a new terminal, requires running app from previous step):

```python load.py```

Enjoy visiting the freshly installed app in the web browser by visiting:

```http://127.0.0.1:8000/municipalities/?format=json```

You can also filter municipalities using a bounding box:

```http://127.0.0.1:8000/municipalities/?in_bbox=4,6,50,60&format=json```
