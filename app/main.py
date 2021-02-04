# coding: utf8

"""
Инцилизация и запуск сервера
"""

from aiohttp import web

from app.configuration import ConfigReader
from gino.ext.aiohttp import Gino
from sqlalchemy.engine.url import URL


def db_make_setup(config):
    db_config = config.data['database']
    dsn = URL(
        drivername=db_config['drivername'],
        username=db_config['username'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port'],
        database=db_config['database']
    )
    return {
        'dsn': dsn,
        **db_config
    }


def main():
    """
    Точка доступа
    :return: None
    """
    config = ConfigReader()
    db = Gino()
    app = web.Application(middlewares=[db])
    db.init_app(
        app=app,
        config=db_make_setup(config)
    )

    web.run_app(
        app=app,
        host=config.data["server"]["host"],
        port=config.data["server"]["port"]
    )


if __name__ == "__main__":
    main()
