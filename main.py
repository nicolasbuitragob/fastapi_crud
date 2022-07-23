from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/docs')


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/get_teams/")
def get_teams(db: Session = Depends(get_db)):
    teams = crud.get_teams(db)
    return teams

@app.get("/team/{team_name}",response_model = schemas.Team)
def get_team(team_name:str, db: Session = Depends(get_db)):
    team = crud.get_team(team_name,db)
    return team



@app.post("/create_team/")
def create_team(team: schemas.Team, db: Session = Depends(get_db)):
    db_team = crud.get_team(team.team_name,db)
    if db_team:
        raise HTTPException(status_code=400, detail="team already in db")
    return crud.create_team(db=db, team=team)


# @app.get("/teams/", response_model=schemas.Teams)
# def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     teams = crud.get_teams(db, skip=skip, limit=limit)
#     return teams

# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items
