import pytest
from typing import Any, Dict
from sqlalchemy.orm import declarative_base


from app.database.app import Database
from app.core.config.app import get_config
  
@pytest.fixture
def settings():
  """ Fixture to get settings of application. """
  return get_config()    
    
@pytest.fixture
def database(settings) -> Dict[str, Any]:
  """ Return a dict with instance of Database class and a Model class for create tables. """
  return {
    'instance': Database(settings.url_database),
    'model': declarative_base()
  }

  
  