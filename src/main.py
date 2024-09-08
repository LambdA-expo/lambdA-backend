from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from config.database import get_db, Base, engine
import models

def init_db():
    print("initializing database")
    Base.metadata.create_all(bind=engine)
    print("database intialized successfully.")

init_db()
app = FastAPI()

@app.get("/")
async def home(db: Session = Depends(get_db)):
    return {"message": "Welcome to Lambda!!"}