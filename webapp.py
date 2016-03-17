import os

import jinja2
import aiohttp_jinja2
from aiohttp import web

import settings
import teabag
import utils


@aiohttp_jinja2.template('main.jinja2')
async def index(request):
    return {}


@aiohttp_jinja2.template('message.jinja2')
async def get_message(request):
    token = request.match_info['token'].encode()
    try:
        message = teabag.get_message(token)
    except FileNotFoundError:
        raise web.HTTPNotFound()
    return {'message': message}


@aiohttp_jinja2.template('url.jinja2')
async def save_message(request):
    data = await request.post()
    try:
        token = teabag.save_message(data['message'])
    except ValueError:
        return web.HTTPFound('/')

    url = '{host}{token}'.format(host=settings.host, token=token)
    return {'url': url}


def main():
    utils.startup_check()

    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/{token}', get_message)
    app.router.add_route('POST', '/save', save_message)

    path = os.path.join( os.path.dirname(__file__), 'static')
    app.router.add_static('/static/', path, name='static')

    web.run_app(app)


if __name__ == '__main__':
    main()


# http://127.0.0.1:8000/30HVbSi5V_wd6QSeYimfkIVW10LkjiY6qxbrg5cz
