from datetime import date
from enum import Enum
from dataclasses import dataclass



class Hobby(Enum):
    READING = "Reading"
    SPORT = "Sports"
    MUSIC = "Music"



@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str  # 'Male' | 'Female' | 'Other'
    phone: str
    date_of_birth: date
    hobbies: list[Hobby]
    subjects: list[str]
    picture: str  # имя файла
    address: str
    state: str
    city: str