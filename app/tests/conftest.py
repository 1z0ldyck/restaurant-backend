import pytest
from typing import Any, Dict
from sqlalchemy.orm import declarative_base


from app.database.app import Database
from app.core.config.test import TestSettings
from app.core.config.app import get_config
  
@pytest.fixture
def settings():
  return get_config()    
    
@pytest.fixture
def database(settings) -> Dict[str, Any]:
  return {
    'instance': Database(settings.url_database),
    'model': declarative_base()
  }

def test_settings():
  settings = get_config()
  assert isinstance(settings, TestSettings)
  
  