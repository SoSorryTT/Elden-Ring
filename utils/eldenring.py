import imp
from venv import create
from requests import session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.dao.character_dao import CharacterDao
from utils.dao.weapon_dao import WeaponDao

class Eldenring:
    def __init__(self, connnection_url="sqlite:///sample.db") -> None:
        engine = create_engine(connnection_url)
        session = sessionmaker(bind=engine)
        self.__db_session = session()

    def character(self):
        return CharacterDao(self.__db_session)

    def weapon(self):
        return WeaponDao(self.__db_session)