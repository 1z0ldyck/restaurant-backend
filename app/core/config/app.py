from enum import Enum
from os import environ
from dotenv import load_dotenv

from config.development import DevSettings 
  
  
def get_config():
  load_dotenv()
  
  environments = {
    "development": DevSettings()
  } 
  
  return environments[environ['ENVIRONMENT'].lower()]