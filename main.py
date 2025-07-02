from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "AI Health Assistant API is running."}

@app.get("/appointments/")
def get_appointments(user_id: int, db: Session = Depends(get_db)):
    # Dummy logic, replace with real ORM query
    return {"user_id": user_id, "appointments": []}

@app.post("/login/")
def login():
    # Add real auth logic
    return {"status": "Login endpoint"}
