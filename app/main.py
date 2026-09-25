from fastapi import FastAPI
from app.routers import signup
from app.database import engine
from app import auth, models

# Add this line so SQLAlchemy builds the 'users' table in PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(signup.router)
app.include_router(auth.router)