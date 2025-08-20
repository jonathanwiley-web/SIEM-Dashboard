# models.py
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    source = Column(String)
    message = Column(String)
    level = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True)
    rule_name = Column(String)
    description = Column(String)
    severity = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

engine = create_engine("sqlite:///siem.db")
Base.metadata.create_all(engine)
