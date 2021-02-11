# coding: utf8
from aiohttp import web
from gino import GinoEngine
import aiohttp_jinja2


@aiohttp_jinja2.template('index.html')
async def index(request: web.Request):
    db: GinoEngine = request.app['db']
    database_statuses = await db.status('SELECT version();')
    return {
        'database_statuses': database_statuses[1][0][0],
        'title': 'database-info'
    }
