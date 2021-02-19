from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.database import db_settings

'postgresql://scott:tiger@localhost/mydatabase'
#
if db_settings.db_driver == "postgresql":
    SQLALCHEMY_DATABASE_URI = "{driver}://{username}:{password}@{host}:{port}/{database}".format(
        driver = db_settings.db_driver,
        username = db_settings.db_username,
        passwrod = db_settings.db_password,
        host = db_settings.db_host,
        port = db_settings.db_port,
        database = db_settings.db_database
    )
else:  #sqlite as default
    SQLALCHEMY_DATABASE_URI = "{driver}://{database}".format(
        driver = db_settings.db_driver,
        database = db_settings.db_database
    )



engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
