from sqlalchemy.orm import Session

import models, schemas

# Teams query
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


#Sponsors query
def get_sponsors(db: Session):
    sponsors  = db.query(models.Sponsor).all()
    return sponsors

def get_sponsor(sponsor_name , db: Session):
    sponsor  = db.query(models.Sponsor).filter(models.Sponsor.sponsor_name == sponsor_name).first()
    return sponsor
     
def create_sponsor(sponsor: schemas.SponsorCreate,db: Session,team_id:int):
    db_sponsor = models.Sponsor(sponsor_name = sponsor.sponsor_name, 
                             sponsor_money = sponsor.sponsor_money)

    db_sponsor.team_id = team_id

    db.add(db_sponsor)
    db.commit()
    db.refresh(db_sponsor)
    return db_sponsor

#Cyclists

def get_cyclists(db: Session):
    cyclists  = db.query(models.Cyclist).all()
    return cyclists

def get_cyclist(cyclist_name , db: Session):
    cyclist  = db.query(models.Cyclist).filter(models.Cyclist.cyclist_name == cyclist_name).first()
    return cyclist
     
def create_cyclist(cyclist: schemas.CyclistCreate,db: Session,team_id:int):
    db_cyclist = models.Cyclist(cyclist_name = cyclist.cyclist_name, 
                             speciality = cyclist.speciality,
                             cyclist_country = cyclist.cyclist_country)

    db_cyclist.team_id = team_id

    db.add(db_cyclist)
    db.commit()
    db.refresh(db_cyclist)
    return db_cyclist


