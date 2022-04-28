from cgitb import text
from sqlalchemy import Column, Integer, Text, null, FLOAT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WeaponModel(Base):
    __tablename__ = "weapon"

    id = Column(Integer, primary_key=True, nullable=False)
    WeaponType = Column(Text, nullable=False)
    WeaponName = Column(Text, nullable=False)
    Str = Column(Integer, nullable=False)
    Dex = Column(Integer, nullable=False)
    Int = Column(Integer, nullable=False)
    Fai = Column(Integer, nullable=False)
    Arc = Column(Integer, nullable=False)
    WeaponWeight = Column(FLOAT, nullable=False)
    WeaponSkill = Column(Text, nullable=False)

    def __repr__(self) -> str:
        return f"<Weapon: (id={self.id},weapon_type={self.WeaponType},weapon_name={self.WeaponName},str={self.Str},dex={self.Dex},int={self.Int},fai={self.Fai},arc={self.Arc},weapon_weight={self.WeaponWeight},weapon_skill={self.WeaponSkill})>"