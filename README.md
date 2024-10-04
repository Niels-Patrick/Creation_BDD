# Brief Creation BDD

There are 2 python scripts:
- One to create a database and its tables, based on a SQL file generated from a MCD/MLD/MPD tool [(drawdb.app)](https://www.drawdb.app/editor).
- A second one to fill the database with data contained in csv files.

Also, the queries_brief.sql file contains the queries used to extract data from the database.

## Usage

1. Open the creation_bdd.py file on a Python IDE (PyCharm, VSCode) and run it. The database will be created as well as its tables.
2. Open the importation_bdd.py file on a Python IDE (PyCharm, VSCode) and run it. The database's tables will be filled with data contained in the 2 csv files.
