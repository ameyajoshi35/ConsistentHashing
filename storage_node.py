import requests


class StorageNode:
    def __init__(self, name=None, host=None):
        self.name = name
        self.host = host

    def fetch_file(self, path):
        return requests.get(f'https://{self.host}:1231/{path}').text

    def put_file(self, path):
        with open(path, 'r') as fp:
            content = fp.read()
            return requests.post(f'https://{self.host}:1231/{path}',
                                 body=content).text