#!/usr/bin/env python3
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database URL
DATABASE_URL = "sqlite:///hospital.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

