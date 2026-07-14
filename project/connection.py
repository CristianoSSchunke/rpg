from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABESE_URL = 'postgresql+psycopg://postgres:123456@127.0.0.1:5432/RPG'

engine = create_engine(
    DATABESE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)