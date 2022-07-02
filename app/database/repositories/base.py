from database.app import database
from core.config import app as configuration

class BaseRepository:
  def __init__(self):
    self.settings = configuration.get_config()
    
  @property
  def session(self):
    return database.session()
    
    