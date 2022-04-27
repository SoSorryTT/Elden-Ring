from models.weapon_model import WeaponModel
from sqlalchemy.orm.session import Session

class WeaponDao:
    def __init__(self, session: Session) -> None:
        self.__session = session

    def get_all_weapon(self):
        return self.__session.query(WeaponModel).all()

    def get_weapon_info(self, id):
        return self.__session.query(WeaponModel).filter(WeaponModel.id==id)[0]

    def get_weapon_by_type(self, weapon_type):
        return self.__session.query(WeaponModel).filter(WeaponModel.weapon_type==weapon_type).all()

    def get_weapon_by_name(self, weapon_name):
        return self.__session.query(WeaponModel).filter(WeaponModel.weapon_name==weapon_name).all()

    def get_weapon_by_weight(self, weapon_weight):
        return self.__session.query(WeaponModel).filter(WeaponModel.weapon_weight==weapon_weight).all()

    def get_weapon_by_weapon_skill(self, weapon_skill):
        return self.__session.query(WeaponModel).filter(WeaponModel.weapon_skill==weapon_skill).all()

    def add_new_weapon(self, weapon: WeaponModel):
        self.__session.add(weapon)
        self.__session.commit()
        print(f"Add weapon : {weapon.weapon_type}, {weapon.weapon_name} to database")
