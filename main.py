from aiohttp import web


def setup_routes(app):
    from app.core.routes import setup_routes as setup_core_routes

    setup_core_routes(app)


def setup_app(app):
    setup_routes(app)

    return app


app = web.Application()

if __name__ == "__main__":
    app = setup_app(app)
    web.run_app(app, port=8000)
