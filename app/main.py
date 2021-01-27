# coding: utf8

"""
Инцилизация и запуск сервера
"""

from aiohttp import web

from app.configuration import ConfigReader


def main():
    """
    Точка доступа
    :return: None
    """
    config_reader = ConfigReader()
    app = web.Application()

    web.run_app(
        app=app,
        host=config_reader.data["server"]["host"],
        port=config_reader.data["server"]["port"]
    )


if __name__ == "__main__":
    main()
