from aiohttp import web

import teabag


async def get_message(request):
    token = request.match_info['token'].encode()

    try:
        message = teabag.get_message(token)
    except FileNotFoundError:
        raise web.HTTPNotFound()

    return web.Response(body=message.encode('utf-8'))


async def save_message(request):
    message = await request.text()

    try:
        token = teabag.save_message(message)
    except ValueError:
        raise web.HTTPBadRequest()

    url = '{host}/api/{token}'.format(host=request.host, token=token)
    return web.Response(body=url.encode('utf-8'))
