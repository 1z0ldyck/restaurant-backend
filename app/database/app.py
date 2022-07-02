from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy_utils import create_database, database_exists

from database.tables import Model
from core.config import app as configuration
from loguru import logger

class Database:
  
  def __init__(self, url: str = None):
    self.url = url
  
  def __engine(self):
    engine = create_engine(self.url)

    if not database_exists(engine.url):
      create_database(engine.url)
    
    return engine
  
  def create_tables(self) -> None:
    Model.metadata.create_all(bind=self.__engine())
    
  def session(self):
    return sessionmaker(bind=self.__engine())
  

settings = configuration.get_config()
database = Database(url=settings.database_url)