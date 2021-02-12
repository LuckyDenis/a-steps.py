# coding: utf8
import typing

import aiohttp.web_app
import gino.ext.aiohttp

from app.configuration import reader

Gino = typing.NewType('Gino', gino.ext.aiohttp)
GinoEngine = typing.NewType('GinoEngine', gino.GinoEngine)
Application = typing.NewType('Application', aiohttp.web_app.Application)
ConfigReader = typing.NewType('ConfigReader', reader.ConfigReader)
