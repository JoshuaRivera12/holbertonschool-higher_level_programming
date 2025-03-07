# SQL More Queries

## Description
This project explores advanced SQL queries, including joins, subqueries, views, and user management. It builds on fundamental SQL knowledge to enhance database querying skills.

## Topics Covered
- **Joins** (INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL OUTER JOIN)
- **Subqueries** (Nested queries for advanced filtering)
- **Views** (Creating and managing virtual tables)
- **User Management** (Granting and revoking privileges)
- **Constraints** (UNIQUE, CHECK, FOREIGN KEY, DEFAULT)

## Files
| File Name        | Description |
|-----------------|-------------|
| `0-privileges.sql`  | Lists all MySQL user privileges |
| `1-create_user.sql`  | Creates a new MySQL user |
| `2-create_read_user.sql` | Grants SELECT privileges to a user |
| `3-force_name.sql`  | Creates a table with a NOT NULL constraint |
| `4-never_empty.sql`  | Adds a DEFAULT value constraint |
| `5-unique_id.sql` | Enforces a UNIQUE constraint |
| `6-states.sql` | Creates a table with a foreign key |
| `7-cities.sql` | Creates a table with multiple constraints |
| `8-cities_of_california_subquery.sql` | Uses a subquery to fetch city names |
| `9-cities_by_state_join.sql` | Uses JOIN to list cities with their states |

## Usage
To execute any SQL script, use:
```sh
mysql -u root -p < filename.sql
```
Replace `filename.sql` with the actual file you want to run.

## Author
Project by **Joshua Rivera**.
