#Imports 
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import IntegrityError
from datetime import datetime

#create your database
engine = create_engine("sqlite:///medicalrecords.db",echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()




    


