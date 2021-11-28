# Udacity Data Engineering Nanodegree Project 1
## Data Modeling with Postgres

### Summary
In this project, I have defined fact and dimension tables for a star schema database. In addition, I have written an ETL script, using Python with Pandas, to transform data stored in JSON format into these tables. 

### How to run the Python scripts
To run this project locally, I have leveraged [onekenken](https://hub.docker.com/r/onekenken/postgres-student-image)'s Postgres image in a docker-compose file. Once you have Docker installed, you can start the container in the background via:

```
docker-compose up &
```

A `requirements.txt` file is provided for ease of gathering dependencies. Once you've created a virtual environment (using Conda, virtualenv or similar), you can run the following scripts to process the JSON logs and JSON metadata.

To create the tables run:

```
python create_tables.py
```

To process to logs and metadata run:

```
python etl.py
```

### Explanation of files

#### data directory
Stores the JSON logs and JSON metadata that will be extracted, transformed, and loaded into the fact and dimension tables of the Postgres database.

#### create_tables.py
Drops (if it exists) but otherwise creates the `sparkify` database. Drops all tables as well as creates them.

#### docker-compose.yml
Docker compose file for ease of setting up Postgres locally.

#### etl.ipynb
Jupyter notebook for prototyping the ETL process.

#### etl.py
ETL script written in Python using Pandas that extracts, transforms and loads JSON logs and metadata into the fact and dimension tables created in `create_tables.py`.

#### requirements.txt
Python dependencies required for the project.

#### sql_queries.py
SQL statements required for the project.

#### test.ipynb
Jupyter notebook for testing the table creation and inserts for the star schema.