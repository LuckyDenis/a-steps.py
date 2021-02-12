# coding: utf8
import logging
from typing import NoReturn

import gino.ext.aiohttp
from aiohttp import web
from aiohttp.web_app import Application

from app.configuration import ConfigReader
from app.configuration import setup_database
from app.configuration import setup_jinja2
from app.configuration import setup_logging
from app.configuration import setup_routes


def setup(config_reader, database, app):
    setup_logging(config_reader.logging_variables())
    setup_database(config_reader.database_variables(), database, app)
    setup_jinja2(config_reader.jinja2_variables(), app)
    setup_routes(app)


def main() -> NoReturn:
    database = gino.ext.aiohttp.Gino()
    app: Application = web.Application(
        middlewares=[
            database,
        ]
    )

    config_reader = ConfigReader()
    config_reader.read()

    setup(config_reader, database, app)

    logger = logging.getLogger('app')
    logger.info(f'Configuration version: {config_reader.version()}')

    server_variables = config_reader.server_variables()
    web.run_app(
        app=app,
        host=server_variables["SERVER_HOST"],
        port=server_variables["SERVER_PORT"],
        access_log=logger
    )


if __name__ == "__main__":
    main()
