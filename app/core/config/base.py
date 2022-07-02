from os import environ
from secrets import token_urlsafe
from dotenv import load_dotenv

class BaseSettings:
  load_dotenv()
  
  environment = environ['ENVIRONMENT']
  
  title: str = 'Restaurant backend'
  version: str = '0.0.0'
  debug: bool = False
  
  database_url: str = environ['DATABASE_URL']
  secret_key: str = token_urlsafe(16)
  api_prefix: str = '/api'
  
  @property
  def settings_fastapi(self):
    return {
      "title": self.title,
      "debug": self.debug,
      "version": self.version
    }
  