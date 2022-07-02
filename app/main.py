from fastapi import FastAPI
from core.config import app as configuration
from core.events import start_application

def create_app():
  
  settings = configuration.get_config()
  
  app = FastAPI(**settings.settings_fastapi)
  
  app.add_event_handler("startup", start_application)
  
  return app