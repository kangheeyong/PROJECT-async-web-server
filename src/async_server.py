import os

from sanic import Sanic
from sanic import response

from charfinder import UnicodeNameIndex


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE_NAME = os.path.join(BASE_DIR, 'http_template.html')
SAMPLE_WORDS = ('bismillah chess cat circled Malayalam digit'
                ' Roman face Ethiopic black mark symbol dot'
                ' operator Braille hexagram').split()

ROW_TPL = '<tr><td>{}</td><th>{}</th><td>{}</td></tr>'
LINK_TPL = '<a href="/?query={0}" title="find &quot;{0}&quot;">{0}</a>'
LINKS_HTML = ', '.join(LINK_TPL.format(word) for word in sorted(SAMPLE_WORDS, key=str.upper))

index = UnicodeNameIndex()

with open(TEMPLATE_NAME) as tpl:
    template = tpl.read()
template = template.replace('{links}', LINKS_HTML)


app = Sanic(__name__)


@app.get('/')
async def route(request):
    query = request.args.get('query', '')
    print('Query: {!r}'.format(query))
    if query:
        descriptions = list(index.find_descriptions(query))
        res = '\n'.join(ROW_TPL.format(*descr) for descr in descriptions)
        msg = index.status(query, len(descriptions))
    else:
        descriptions = []
        res = ''
        msg = 'Enter words describing characters.'

    html = template.format(query=query, result=res, message=msg)

    print('Sending {} results'.format(len(descriptions)))
    return response.html(html)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
