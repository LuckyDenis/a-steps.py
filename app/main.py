# coding: utf8

import gino.ext.aiohttp
from aiohttp import web

from app.configuration import ConfigReader
from app.configuration.database import setup_database
from app.configuration.routes import setup_routes
from app.configuration.jinja import setup_jinja2


def main():
    database = gino.ext.aiohttp.Gino()
    app = web.Application(middlewares=[database])

    config_reader = ConfigReader()
    config_reader.read()

    setup_database(config_reader.database_variables(), database, app)
    setup_jinja2(config_reader.jinja2_variables(), app)
    setup_routes(app)

    server_variables = config_reader.server_variables()
    web.run_app(
        app=app,
        host=server_variables["SERVER_HOST"],
        port=server_variables["SERVER_PORT"]
    )


if __name__ == "__main__":
    main()
