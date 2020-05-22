import os
import asyncio
import json

from sanic import Sanic
from sanic import response
from aiocache import cached

from charfinder import UnicodeNameIndex
from server_constant import TEMPLATE_DIR, TEMPLATE_NAME, ROW_TPL, LINKS_HTML


index = UnicodeNameIndex()

with open(TEMPLATE_NAME) as tpl:
    template = tpl.read()
template = template.replace('{links}', LINKS_HTML)


app = Sanic(__name__)
for filename in os.listdir(TEMPLATE_DIR):
    app.static(os.path.join('template', filename), os.path.join(TEMPLATE_DIR, filename))


@cached(ttl=3600)
async def get_UnicodeNameIndex(query, start=0, end=None):
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(*descr) for descr in descriptions[start:end])
        msg = index.status(query, len(descriptions))
        await asyncio.sleep(1)
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'

    return descriptions, res, msg


@app.get('/')
async def route(request):
    query = request.args.get('query', '')
    print('Query: {!r}'.format(query))

    descriptions, res, msg = await get_UnicodeNameIndex(query, 0, 100)
    html = template.format(query=query, result=res, message=msg)

    print('Sending {} results'.format(len(descriptions)))
    return response.html(html)


@app.websocket('/feed')
async def feed(request, ws):
    cnt = 1
    while True:
        data = json.loads(await ws.recv())
        query = data['query']
        descriptions, res, msg = await get_UnicodeNameIndex(query, cnt*100, (cnt+1)*100)
        if len(descriptions) > cnt*100:
            msg = 'Sending: {} -> {}~{}'.format(query,
                                                cnt*100,
                                                (cnt+1)*100 if len(descriptions) > (cnt+1)*100 else len(descriptions))
            print(msg)
            await ws.send(res)
            cnt += 1
        else:
            msg = 'Finish: {}'.format(query)
            print(msg)
            break


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
