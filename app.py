import jinja2
import aiohttp_jinja2
from aiohttp import web

import settings
import storage
import cryptographer
import utils


@aiohttp_jinja2.template('main.jinja2')
async def index(request):
    return {}


@aiohttp_jinja2.template('message.jinja2')
async def get_message(request):
    token = request.match_info['token'].encode()
    message_id = token[:settings.message_id_size].decode('utf-8')
    key = token[settings.message_id_size:].decode('utf-8')

    try:
        ciphertext = storage.load_ciphertext(message_id)
    except storage.FileNotFound:
        raise web.HTTPNotFound()

    message = cryptographer.decrypt(key, ciphertext)
    storage.remove_message(message_id)
    return {'message': message}


@aiohttp_jinja2.template('url.jinja2')
async def save_message(request):
    data = await request.post()
    message = data['message']

    key, ciphertext = cryptographer.encrypt(message)
    message_id = storage.save_ciphertext(ciphertext)

    url = '{host}{message_id}{key}'.format(
        host=settings.host, message_id=message_id, key=key)
    return {'url': url}


def main():
    utils.startup_check()

    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/{token}', get_message)
    app.router.add_route('POST', '/save', save_message)

    web.run_app(app)

# http://127.0.0.1:8000/30HVbSi5V_wd6QSeYimfkIVW10LkjiY6qxbrg5cz

if __name__ == '__main__':
    main()
