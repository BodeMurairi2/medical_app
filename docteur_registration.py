#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the database URL
DATABASE_URL = "sqlite:///doctors_data.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
