from sqlalchemy.orm import Session

from . import models, schemas




def get_teams(db: Session):
    teams  = db.query(models.Team).all()
    return teams

def get_team(team_name , db: Session):
    team  = db.query(models.Team).filter(models.Team.team_name == team_name).first()
    return team
     
def create_team(team: schemas.TeamCreate,db: Session):
    db_team = models.Team(country = team.country, 
                          team_name = team.team_name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

# def get_stage(db: Session, stage_id: int):
#     return db.query(models.Stage).filter(models.Stage.id == stage_id).first()

# def get_cyclist(db: Session, cyclist_id):
#     return db.query(models.Cyclist).filter(models.Cyclist.id == cyclist_id).first()


# def create_cyclist(db: Session, cyclist: schemas.CyclistCreate):
#     db_cyclist = models.Cyclist(cyclist_name = cyclist.cyclist_name, 
#                                 cyclist_time = cyclist.cyclist_time,
#                                 speciality = cyclist.speciality,
#                                 cyclist_country = cyclist.cyclist_country)
#     db.add(db_cyclist)
#     db.commit()
#     db.refresh(db_cyclist)
#     return db_cyclist

##missing creat sponsor