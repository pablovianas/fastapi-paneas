# FastAPI - Paneas

The application is a user management system with CRUD, JWT authentication, user permissions, integration with PostgreSQL via SQLAlchemy and Alembic for migrations. The API is documented using Swagger, with example requests and responses. Dockerization is facilitated by Dockerfile and docker-compose, ensuring ease of deployment and environment consistency.

# Tecnologies

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker

# How to setup it?

- Download zip aplication from github or use `git clone "url"`
- Create a virtual environment with the following command: `python -m venv venv`
- After that, we need to active that environment: `venv\Scripts\activate` if you're using Windows.
- Now we build the Dockerfile: `docker-compose build`
- Then we run docker-compose file: `docker-compose up`
- After we started the container, we need to create the database:
Go to http://localhost:5050/browser/ and login with:

```
admin@admin.com
admin@paneas
```
And then, server -> right click -> register -> server 
In general tab, you can write anything as name and go to conection tab and fill with those values:
```
hostname/address: db
Port: 5432
username: postgres
password: paneas
```
And click save. Don't forget to connect on db, just click on db name, database and user_db

- Next step will be run the migrations to create user table:
`docker-compose run app alembic revision --autogenerate -m "Create users table"`
- And finally, run migrations to database: 
`docker-compose run app alembic upgrade head`

# API Documentation

- Documentation is available at: http://localhost:8080/docs#/
- I recommend to create an user first, and then generate token and click on Authorize button
- Fill the username (email) and password and client_secret with generated token
- Then, you can try test PUT and DELETE methods
- If you try with user role, will return 401 - Unauthorized

# API Routes

- /users/create - Method: POST

Example Schema: 
```
  name: str
  email: str
  password: str
  role: Optional[str] = None
  isActive: bool
```
- /users/all  - Method: GET

Retrieve all users from database

- users/{id} - Method: PUT - Need admin permission to update

Update an user from database

Example Schema:

```
  name: Optional[str] = None
  email: Optional[str] = None
  password: Optional[str] = None
  role: Optional[str] = None
  isActive: Optional[bool] = None
```
- users/{id} - Method: DELETE - Need admin permission to delete

Remove an user from database


- /token

Generate JWT access token 


