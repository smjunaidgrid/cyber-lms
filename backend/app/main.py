from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI(title="Cybersecurity Awareness Platform")

# Create DB tables automatically (temporary for dev)
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Cyber Training API Running....."}
