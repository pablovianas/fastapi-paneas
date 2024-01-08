import os
import uvicorn
import sys

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from dotenv import load_dotenv

from src.routes import users
from src.routes import auth
# from .src.routes.users import router


sys.path.append(".") 


load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(users.router)
app.include_router(auth.router)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)