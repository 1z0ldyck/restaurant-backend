import pytest
from sqlalchemy import Column, String, Integer


def test_create_tables(database):
    
    Model = database.get('model')
    database = database.get('instance')
    
    class MyTestTable(Model):
        __tablename__ = 'my_test_table'
        
        id = Column(Integer, primary_key=True)
        name = Column(String(255), nullable=False)
        
    
    database.create_tables()
        
    assert list(Model.metadata.tables.keys()) == ['my_test_table']        
    
    
        
    
    
    
