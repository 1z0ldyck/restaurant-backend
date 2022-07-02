from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session 
from loguru import logger
from pydantic import BaseModel

from database.tables import Model

class ConfigurationModel(BaseModel):
  database_url: str

class Database:
  
  def __init__(self, config: ConfigurationModel):
    self.config = config
    self.__create_tables()
  
  def __engine(self):
    return create_engine(self.config.database_url)
  
  def __create_tables(self) -> None:
    Model.metadata.create_all(bind=self.__engine)
    
  def session(self):
    return sessionmaker(bind=self.__engine())