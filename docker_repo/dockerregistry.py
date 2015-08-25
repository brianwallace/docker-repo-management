import click
import requests


class DockerRegistry():
    """Utility class for making URL requests."""

    def __init__(self, base_url):
        self.base_url = base_url

    def _make_request(self, method, url, data, headers, options):
        if options is None:
            options = {}
        if headers is None:
            headers = {'Content-Type': 'application/json'}

        if method == 'GET':
            return requests.get(
                "".join((self.base_url, url)),
                data=data,
                #auth=(self.username, self.password),
                headers=headers,
                params=options)
        elif method == 'PUT':
            return requests.put(
                "".join((self.base_url, url)),
                data=data,
                #auth=(self.username, self.password),
                headers=headers,
                params=options)
        elif method == 'POST':
            return requests.post(
                "".join((self.base_url, url)),
                data=data,
                #auth=(self.username, self.password),
                headers=headers,
                params=options)
        elif method == 'DELETE':
            return requests.delete(
                "".join((self.base_url, url)),
                data=data,
                #auth=(self.username, self.password),
                headers=headers,
                params=options)
        else:
            raise click.UsageError(
                'Unsupported request type: {0}'.format(method))

    def get(self, url, data=None, headers=None, options=None):
        return self._make_request(
            method='GET',
            url=url,
            data=data,
            headers=headers,
            options=options)

    def put(self, url, data=None, headers=None, options=None):
        return self._make_request(
            method='PUT',
            url=url,
            data=data,
            headers=headers,
            options=options)

    def post(self, url, data=None, headers=None, options=None):
        return self._make_request(
            method='POST',
            url=url,
            data=data,
            headers=headers,
            options=options)

    def delete(self, url, data=None, headers=None, options=None):
        return self._make_request(
            method='DELETE',
            url=url,
            data=data,
            headers=headers,
            options=options)
