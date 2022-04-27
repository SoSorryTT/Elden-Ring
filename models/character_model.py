from cgitb import text
from sqlalchemy import Column, Integer, Text, null, FLOAT
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class EldenringModel(Base):
    __tablename__ = "character"

    id = Column(Integer, primary_key=True, nullable=False)
    character_id = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    str = Column(Integer, nullable=False)
    dex = Column(Integer, nullable=False)
    int = Column(Integer, nullable=False)
    fai = Column(Integer, nullable=False)
    arc = Column(Integer, nullable=False)
    weight = Column(FLOAT, nullable=False)
    owner_id = Column(Text)

    def __repr__(self) -> str:
        return f"<Character: (id={self.id},character_id={self.character_id},str={self.str},dex={self.dex},int={self.int},fai={self.fai},arc={self.arc},weight={self.weight},owner_id={self.owner_id})"