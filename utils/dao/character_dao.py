from models.character_model import CharacterModel
from sqlalchemy.orm.session import Session

class CharacterDao:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_all_character(self):
        return self.__session.query(CharacterModel).all()

    def get_character_info(self, id):
        return self.__session.query(CharacterModel).filter(CharacterModel.id==id)[0]

    def get_character_by_characterID(self, chracter_id):
        return self.__session.query(CharacterModel).filter(CharacterModel.character_id==chracter_id).all()

    def get_character_by_weaponID(self, owner_id):
        return self.__session.query(CharacterModel).filter(CharacterModel.owner_id==owner_id).all()

    def add_new_character(self, character: CharacterModel):
        self.__session.add(character)
        self.__session.commit()
        print(f"Add Character : {character.character_id} to database")