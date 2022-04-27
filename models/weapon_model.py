from cgitb import text
from sqlalchemy import Column, Integer, Text, null, FLOAT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WeaponModel(Base):
    __tablename__ = "weapon"

    id = Column(Integer, primary_key=True, nullable=False)
    weapon_type = Column(Text, nullable=False)
    weapon_name = Column(Text, nullable=False)
    str = Column(Integer, nullable=False)
    dex = Column(Integer, nullable=False)
    int = Column(Integer, nullable=False)
    fai = Column(Integer, nullable=False)
    arc = Column(Integer, nullable=False)
    weapon_weight = Column(FLOAT, nullable=False)
    weapon_skill = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Weapon: (id={self.id},weapon_type={self.weapon_type},weapon_name={self.weapon_name},str={self.str},dex={self.dex},int={self.int},fai={self.fai},arc={self.arc},weapon_weight={self.weapon_weight},weapon_skill={self.weapon_skill})"