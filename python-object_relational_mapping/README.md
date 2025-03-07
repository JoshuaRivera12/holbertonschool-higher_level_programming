# Python - Object-Relational Mapping (ORM)

## Description
This project introduces **Object-Relational Mapping (ORM)**, which allows interaction with databases using Python objects instead of raw SQL queries. The primary focus is on using **SQLAlchemy**, a powerful Python ORM library.

## Topics Covered
- **Introduction to ORM** (Benefits and concepts)
- **SQLAlchemy Basics** (Installation, engine, session management)
- **Defining Models** (Mapping Python classes to database tables)
- **CRUD Operations** (Creating, Reading, Updating, Deleting records)
- **Relationships** (One-to-many, many-to-many relationships)
- **Querying with SQLAlchemy** (Filtering, ordering, and joining tables)
- **Migrations** (Managing database schema changes with Alembic)

## Files
| File Name                   | Description |
|-----------------------------|-------------|
| `0-select_states.py`        | Lists all states from the database using SQLAlchemy |
| `1-filter_states.py`        | Lists states with a specific name filter |
| `2-my_filter_states.py`     | Filters states using user input |
| `3-my_safe_filter_states.py` | Secure filtering against SQL injection |
| `4-cities_by_state.py`      | Lists all cities with their corresponding states |
| `5-relationship_state.py`   | Demonstrates ORM relationships between tables |
| `6-relationship_cities.py`  | Adds a new city to a state using ORM |

## Usage
To execute any Python script with SQLAlchemy, run:
```sh
python3 filename.py username password database_name
```
Replace `filename.py` with the actual script name, and provide your database credentials.

## Author
Project by **Holberton School**.


