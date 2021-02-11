from app.algorithms.views import index


def setup_routes(app):
    app.router.add_get('/', index, name='index')
    app.router.add_get('/index', index)
    app.router.add_get('/index.html', index)
