import jinja2
import aiohttp_jinja2
from aiohttp import web

import settings
import teabag


@aiohttp_jinja2.template('main.jinja2')
async def index(request):
    return {}


async def get_message(request):
    token = request.match_info['token'].encode()
    try:
        message = teabag.get_message(token)
        context = {'message': message}
        response = aiohttp_jinja2.render_template(
            'message.jinja2', request, context)
    except FileNotFoundError:
        response = _get_404_response(request)
    return response


@aiohttp_jinja2.template('url.jinja2')
async def save_message(request):
    data = await request.post()
    try:
        token = teabag.save_message(data['message'])
    except ValueError:
        return web.HTTPFound('/')

    url = '{host}{token}'.format(host=settings.host, token=token)
    return {'url': url}


def _get_404_response(request):
    response = aiohttp_jinja2.render_template('404.jinja2', request, {})
    response.set_status(404)
    return response