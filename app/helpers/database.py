import os

from instance.config import app_config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

configuration_env = os.getenv('FLASK_ENV')
database_uri = app_config.get(configuration_env).SQLALCHEMY_DATABASE_URI
engine = create_engine(database_uri)
db_session = sessionmaker(bind=engine)
Base = declarative_base()
