from sqlalchemy import Column, String, Integer

from db.base_class import Base


class Sample(Base):
    __tablename__ = "sample"

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String)
