from typing import List, Union
from datetime import datetime
from pydantic import BaseModel


class Stage(BaseModel):
    id : int
    stage_time : datetime.time
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
    cyclist_time : datetime.time
    speciality : str
    cyclist_country : str
    team_id : int

    class Config:
        orm_mode = True


class CyclistCreate(Cyclist):
    pass


class Team(BaseModel):
    id: int
    country: str
    team_name: str
    coach_id : int

    class Config:
        orm_mode = True


class Coach(BaseModel):
    id: int
    coach_name: str
    coach_country: str
    
    class Config:
        orm_mode = True


class Sponsor(BaseModel):
    id: int
    sponsor_name: str
    sponsor_money: str
    team_id : int

    class Config:
        orm_mode = True
