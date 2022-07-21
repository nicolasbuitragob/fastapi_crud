from sqlalchemy.orm import Session

from . import models, schemas


def get_stage(db: Session, stage_id: int):
    return db.query(models.Stage).filter(models.Stage.id == stage_id).first()

def get_cyclist(db: Session, cyclist_id):
    return db.query(models.Cyclist).filter(models.Cyclist.id == cyclist_id).first()

def get_coach(db: Session, coach_id):
    return db.query(models.Coach).filter(models.Coach.id == coach_id).first()

def create_coach(db: Session, coach: schemas.CoachCreate):
    db_coach = models.Coach(coach_name = coach.coach_name, 
                          coach_country = coach.coach_country)
    db.add(db_coach)
    db.commit()
    db.refresh(db_coach)
    return db_coach

def create_team(db: Session, team: schemas.TeamCreate):
    db_team = models.Team(country = team.country, 
                          team_name = team.team_name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def create_cyclist(db: Session, cyclist: schemas.CyclistCreate):
    db_cyclist = models.Cyclist(cyclist_name = cyclist.cyclist_name, 
                                cyclist_time = cyclist.cyclist_time,
                                speciality = cyclist.speciality,
                                cyclist_country = cyclist.cyclist_country)
    db.add(db_cyclist)
    db.commit()
    db.refresh(db_cyclist)
    return db_cyclist

##missing creat sponsor