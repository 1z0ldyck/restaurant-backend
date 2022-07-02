from fastapi import FastAPI
from core.config import app as configuration

def create_app():
  
  settings = configuration.get_config()
  
  app = FastAPI(**settings.settings_fastapi)
  
  return app