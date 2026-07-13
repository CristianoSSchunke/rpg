from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABESE_URL = 'postgresql://postgres:CRIZAODEV@localhost:5432/rpg'

engine = create_engine(DATABESE_URL)

SessionLocal = sessionmaker(bind=engine)