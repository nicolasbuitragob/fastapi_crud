from datetime import time
from pydantic import BaseModel


class Stage(BaseModel):
    id : int
    stage_time : time
    stage_type : str
    distance_km : float
    start : str
    finish : str
    cyclist_id: int

    class Config:
        orm_mode = True

class StageCreate(Stage):
    pass


class Cyclist(BaseModel):
    id: int
    cyclist_name : str
    cyclist_time : time
    speciality : str
    cyclist_country : str
    team_id : int

    class Config:
        orm_mode = True


class CyclistCreate(Cyclist):
    pass


class Team(BaseModel):
    country: str
    team_name: str

    class Config:
        orm_mode = True

class TeamCreate(Team):
    pass


class Sponsor(BaseModel):
    id: int
    sponsor_name: str
    sponsor_money: str
    team_id : int

    class Config:
        orm_mode = True

class SponsrCreate(Sponsor):
    pass
