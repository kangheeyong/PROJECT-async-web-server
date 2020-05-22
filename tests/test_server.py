import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'src'))

from server import app


def test_status_200():
    params = {'query': 'chess'}
    request, response = app.test_client.get('/', params=params)
    assert response.status == 200


