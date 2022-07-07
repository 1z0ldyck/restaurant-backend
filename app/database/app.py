from typing import Union
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy_utils import create_database, database_exists
from loguru import logger

from core.config import app as configuration
from models import Model

class Database:
  
  def __init__(self, url: Union[str, None] = None):
    self.url = url
  
  def __engine(self):
    if self.url:
      engine = create_engine(self.url)

      if not database_exists(engine.url):
        create_database(engine.url)
    
      return engine
    else:
      logger.error('Could not create a engine. The url is not valid.')
      
  def create_tables(self) -> None:
    
    # this code import all models and create tables in the database if not exists.
    from models import tables
    
    Model.metadata.create_all(bind=self.__engine())
    
  def session(self):
    return sessionmaker(bind=self.__engine())
  

settings = configuration.get_config()
database = Database(url=settings.database_url)