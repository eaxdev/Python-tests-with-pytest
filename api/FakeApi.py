import requests

from exceptions import ExpectedStatusCodeError


class FakeApi(object):

    def get_all_fake_todos(self):
        request = requests.get(url='https://jsonplaceholder.typicode.com/todos/')
        if request.status_code != 200:
            raise ExpectedStatusCodeError
        return request.json()
