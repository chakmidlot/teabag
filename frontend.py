import jinja2
import aiohttp_jinja2
from aiohttp import web

import settings
import teabag


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
