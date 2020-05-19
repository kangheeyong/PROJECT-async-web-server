import os

from sanic import Sanic
from sanic import response

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_NAME = os.path.join(BASE_DIR, 'http_template.html')
CONTENT_TYPE = 'text/html; charset=UTF-8'
SAMPLE_WORDS = ('bismillah chess cat circled Malayalam digit'
                ' Roman face Ethiopic black mark symbol dot'
                ' operator Braille hexagram').split()

LINK_TPL = '<a href="/?query={0}" title="find &quot;{0}&quot;">{0}</a>'
LINKS_HTML = ', '.join(LINK_TPL.format(word) for word in sorted(SAMPLE_WORDS, key=str.upper))

with open(TEMPLATE_NAME) as tpl:
    template = tpl.read()
template = template.replace('{links}', LINKS_HTML)


app = Sanic(__name__)


@app.get('/')
async def route(request):
    query = request.args.get('query', '')
    res = ''
    msg = 'Enter words describing characters.'

    html = template.format(query=query, result=res, message=msg)
    return response.html(html)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
