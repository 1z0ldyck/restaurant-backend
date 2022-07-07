from os import environ
from dotenv import load_dotenv

from core.config.development import DevSettings 
from core.config.test import TestSettings
  
  
def get_config():
  load_dotenv()
  
  environments = {
    "development": DevSettings(),
    "testing": TestSettings(),
  } 
  
  return environments[environ['ENVIRONMENT'].lower()]