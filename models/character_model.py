from cgitb import text
from sqlalchemy import Column, Integer, Text, null, FLOAT, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CharacterModel(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, nullable=False)
    CharacterID = Column(Text, nullable=False)
    Gender = Column(Text, nullable=False)
    Str = Column(Integer, nullable=False)
    Dex = Column(Integer, nullable=False)
    Int = Column(Integer, nullable=False)
    Fai = Column(Integer, nullable=False)
    Arc = Column(Integer, nullable=False)
    Weight = Column(FLOAT, nullable=False)
    owner_id = Column(Integer, ForeignKey("weapon.id"), nullable=True)

    def __repr__(self) -> str:
        # return f"<Character: (id={self.id},character_id={self.character_id},str={self.str},dex={self.dex},int={self.int},fai={self.fai},arc={self.arc},weight={self.weight},owner_id={self.owner_id})>"
        return f"<Character: (id={self.id},character_id={self.CharacterID}, gender={self.Gender}s,str={self.Str},dex={self.Dex},int={self.Int},fai={self.Fai},arc={self.Arc},weight={self.Weight}, owner_id={self.owner_id})>"