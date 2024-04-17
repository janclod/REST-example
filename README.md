## REST API

Basic example of REST API to consume and return geospatial data.

## How to build

### Requirements

#### Database backend

Need to have a running instance of Postgresql.

The Postgresql instance must be reachable from the location where the app is running on standard port (`5432`).

The Postgresql instance must have a username `geodjango` (password `geodjango`).

The Postgresql instance must contain a DB named `test`.

The `geodjango` username must own the `test` DB and have create/read/write rights.

#### Python packages

- python
- django
- rest_framework
- rest_framework_gis
- requests
- psycopg2

### Step-by-step (for developers)

Download, install deps, run server, migrate.
Launch script or example post/get request.
