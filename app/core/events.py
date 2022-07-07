from database.app import database
from loguru import logger

def start_application():
  
  # Create database tables
  logger.info("Creating database tables...")
  database.create_tables()
  
  