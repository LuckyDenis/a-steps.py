# coding: utf8
from sqlalchemy.engine.url import URL
from app.typehints import Gino, Application
from typing import NoReturn, Dict, AnyStr


def make_url(database_variables: Dict[AnyStr, AnyStr]) -> URL:
    return URL(
        drivername=database_variables['DATABASE_DRIVERNAME'],
        username=database_variables['DATABASE_USERNAME'],
        password=database_variables['DATABASE_PASSWORD'],
        host=database_variables['DATABASE_HOST'],
        port=database_variables['DATABASE_PORT'],
        database=database_variables['DATABASE_NAME']
    )


def setup_database(
        database_variables: Dict[AnyStr, AnyStr],
        database: Gino, app: Application) -> NoReturn:
    dsn = make_url(database_variables)

    database.init_app(
        app=app,
        config={
            'dsn': dsn,
            'drivername': database_variables['DATABASE_DRIVERNAME'],
            'echo': database_variables['DATABASE_ECHO'],
            'pool_min_size': database_variables['DATABASE_POOL_MIN_SIZE'],
            'pool_max_size': database_variables['DATABASE_POOL_MAX_SIZE'],
            'ssl': database_variables['DATABASE_SSL'],
            'retry_limit': database_variables['DATABASE_RETRY_LIMIT'],
            'retry_interval': database_variables['DATABASE_RETRY_INTERVAL']
        }
    )
