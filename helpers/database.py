import os

from instance.config import app_config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


configuration_env = os.getenv('FLASK_ENV')
database_uri = app_config.get(configuration_env).SQLALCHEMY_DATABASE_URI
engine = create_engine(database_uri)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
