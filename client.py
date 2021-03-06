# client.py
import requests

class MyAPIClient(object):
    """A simple API client for querying corgi data"""

    base_url = 'http://api.corgidata.com'
    version = 'v1'

    def _make_uri(self, resource):
        """
        Construct the URL for a resource based on the API class's parameters
        """
        return '/'.join([self.base_uri, self.version, resource])

    def _get(self, url, retries=3):
        """Make a GET request to an endpoint defined by 'url'"""
        while retries > 0:
            try:
                response = requests.get(url=url)
                try:
                    response.raise_for_status()
                    return response.json()
                except requests.exceptions.HTTPError as e:
                    self._handle_http_error(e)
            except (requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout) as e:
                retries -= 1
                if not retries:
                    self._handle_connection_error(e)

    def get_breed_info(self, breed):
        """Return information about a specific breed of corgi"""
        resource = '/'.join(['breeds', breed])
        url = self._make_url(resource=resource)
        response = self._get(url=url)
        return response

    def _handle_connection_error(self, e):
        """Handle a persistent connection error or timeout"""
        raise requests.exceptions.ConnectionError


    def _handle_http_error(self, e):
        """Handle a HTTP error"""
        pass