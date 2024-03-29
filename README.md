# FastAPI - Paneas

The application is a user management system with CRUD, JWT authentication, user permissions, integration with PostgreSQL via SQLAlchemy and Alembic for migrations. The API is documented using Swagger, with example requests and responses. Dockerization is facilitated by Dockerfile and docker-compose, ensuring ease of deployment and environment consistency.

# Tecnologies

- FastAPI
- SQLAlchemy
- Alembic
- PostgreSQL
- Docker
- Prometheus
- Grafana
- Celery
- RabbitMQ

# .env example
You can use the following environment variables to run project
I'm using gmail smtp service to send emails when users are created, so you need to configure before using it.

```
DATABASE_URL=postgresql+psycopg2://postgres:paneas@db:5432/user_db
DB_USER=postgres
DB_PASSWORD=paneas
DB_NAME=user_db
PGADMIN_DEFAULT_EMAIL=admin@admin.com
PGADMIN_DEFAULT_PASSWORD=admin@paneas
SECRET_KEY="generate a random secret key"
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
EMAIL_TOKEN= "generate a secret key from gmail service"
YOUR_GMAIL="use some gmail account"
```

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

# Using Grafana

- In order to use Grafana, you need to http://localhost:3000/ and login with credentials:

```
admin
admin
```

- Add the datasource Prometheus with those params and click on Save & test:

```
Name: Prometheus
URL: http://prometheus:9090
Access: Server (Default)
Scrape interval: 15s
HTTP Method: GET
HTTP Auth: None
Basic Auth: None
With Credentials: No
TLS Client Auth: None
TLS CA Certificate: None
```

