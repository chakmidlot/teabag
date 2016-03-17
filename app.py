import aiohttp_jinja2
import jinja2
from aiohttp import web

import cryptographer
import settings
import storage


@aiohttp_jinja2.template('main.jinja2')
async def index(request):
    return {}


@aiohttp_jinja2.template('message.jinja2')
async def get_message(request):
    token = request.match_info['token'].encode()

    message_id = token[:settings.message_id_size].decode('utf-8')
    key = token[settings.message_id_size:].decode('utf-8')

    ciphertext = storage.load_ciphertext(message_id)
    message = cryptographer.decrypt(key, ciphertext)

    return {'message': message}


@aiohttp_jinja2.template('url.jinja2')
async def save_message(request):
    data = await request.post()

    message = data['message']

    key, ciphertext = cryptographer.encrypt(message)

    message_id = storage.save_ciphertext(ciphertext)

    url = settings.host + message_id + key
    return {'url': url}


app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/{token}', get_message)
app.router.add_route('POST', '/save', save_message)

web.run_app(app)

# http://127.0.0.1:8000/30HVbSi5V_wd6QSeYimfkIVW10LkjiY6qxbrg5cz
