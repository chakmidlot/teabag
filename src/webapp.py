import os

import aiohttp_jinja2
import jinja2
from aiohttp import web

import api
import frontend
import utils


def add_routes(app):
    app.router.add_route('GET', '/', frontend.index)
    app.router.add_route('GET', '/{token}', frontend.get_message_intermediate)
    app.router.add_route('GET', '/message/{token}', frontend.get_message)
    app.router.add_route('GET', '/api/{token}', api.get_message)
    app.router.add_route('POST', '/save', frontend.save_message)
    app.router.add_route('POST', '/api/save', api.save_message)


def main():
    utils.startup_check()

    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

    path = os.path.join(os.path.dirname(__file__), 'static')
    app.router.add_static('/static/', path, name='static')

    add_routes(app)
    return app


app = main()

if __name__ == '__main__':
    web.run_app(app)


# http://127.0.0.1:8080/30HVbSi5V_wd6QSeYimfkIVW10LkjiY6qxbrg5cz
