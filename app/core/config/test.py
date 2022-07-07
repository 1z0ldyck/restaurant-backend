from core.config.base import BaseSettings

class TestSettings(BaseSettings):
  url_database = 'sqlite:///:memory:'
  