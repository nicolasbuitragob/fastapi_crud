from sqlalchemy import  Column, ForeignKey, Integer, String, Time, Float
from database import Base


class Stage(Base):
    __tablename__ = "stages"

    id = Column(Integer, primary_key=True, index=True)
    stage_time = Column(Time)
    stage_type = Column(String)
    distance_km = Column(Float)
    start = Column(String)
    finish = Column(String)
    cyclist_id = Column(Integer, ForeignKey("cyclists.id"))


class Cyclist(Base):
    __tablename__ = "cyclists"

    id = Column(Integer, primary_key=True, index=True)
    cyclist_name = Column(String)
    cyclist_time = Column(Time, default=None)
    speciality = Column(String)
    cyclist_country = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String)
    team_name = Column(String)


class Sponsor(Base):
    __tablename__ = "sponsors"

    id = Column(Integer, primary_key=True, index=True)
    sponsor_name = Column(String)
    sponsor_money = Column(Float)
    team_id = Column(Integer, ForeignKey("teams.id"))
