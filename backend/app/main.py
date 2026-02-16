from fastapi import FastAPI

app = FastAPI(title="Interactive Cybersecurity Awareness Training Platform")

@app.get("/")
def root():
    return {"message" : "Cyber Training API building"}
