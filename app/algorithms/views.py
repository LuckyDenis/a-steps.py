# coding: utf8
from aiohttp import web
import aiohttp_jinja2
from app.typehints import GinoEngine
import logging


logger = logging.getLogger(__name__)


@aiohttp_jinja2.template('index.html')
async def index(request: web.Request):
    db: GinoEngine = request.app['db']
    database_statuses = await db.status('SELECT version();')
    return {
        'database_statuses': database_statuses[1][0][0],
        'title': 'database-info'
    }
