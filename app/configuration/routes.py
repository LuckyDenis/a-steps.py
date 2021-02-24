# coding: utf8
from app.algorithms.views import index
from app.typehints import Application
from typing import NoReturn


def setup_routes(app: Application) -> NoReturn:
    app.router.add_get('/', index, name='index')
    app.router.add_get('/index', index)
    app.router.add_get('/index.html', index)
    app.router.add_static(
        '/static/', path='templates/static/', name='static')
