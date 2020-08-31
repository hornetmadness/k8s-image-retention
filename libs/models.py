from libs.config import config
# import arrow
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

print(config)


def connect_db():
    if not database_exists(config.database.connection):
        create_database(config.database.connection)
    db = create_engine(config.database.connection, echo=config.database.debug)
    return db


Base = declarative_base()


class Images(Base):
    __tablename__ = "images"
    uri = Column(String(255), nullable=False, primary_key=True)
    added = Column(DateTime, nullable=False, default=func.now())
    last_seen = Column(DateTime, nullable=False, default=func.now(), index=True)
    disabled = Column(Integer, default=0, nullable=False)


engine = connect_db()
Images.__table__.create(bind=engine, checkfirst=True)
