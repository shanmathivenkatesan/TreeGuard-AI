from sqlalchemy import Column, Integer, String
from database import Base

class Tree(Base):
    __tablename__ = "trees"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    age = Column(Integer)
    health_status = Column(String)
    lifecycle_stage = Column(String)
    guardian = Column(String, default="Unassigned")
    
class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    tree_id = Column(Integer)
    message = Column(String)
    status = Column(String)
