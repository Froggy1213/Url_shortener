import time
import validators
from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from sqlalchemy.exc import OperationalError 

from . import models, schemas, crud, database


app = FastAPI()


# models.Base.metadata.create_all(bind=database.engine)

while True:
    try:
        models.Base.metadata.create_all(bind=database.engine)
        print("Database connected and tables created!")
        break
    except OperationalError:
        print("Database not ready, waiting 2 seconds...")
        time.sleep(2)


@app.get("/")
def read_root():
    return "Welcome to the URL Shortener API!"


@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLCreate, db: Session = Depends(database.get_db)):
    
    if not validators.url(url.target_url):
        raise HTTPException(status_code=400, detail="Your provided URL is not valid")

    db_url = crud.create_db_url(db=db, url=url)
    return db_url


@app.get("/{url_key}")
def forward_to_target_url(url_key: str, request: Request, db: Session = Depends(database.get_db)):
    db_url = crud.get_db_url_by_key(db, url_key)
    
    if db_url:
        return RedirectResponse(url=db_url.target_url)
    else:
    
        raise HTTPException(status_code=404, detail=f"URL '{url_key}' not found")