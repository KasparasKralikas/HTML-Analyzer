import html_to_json
import requests

class HTMLParser:

    _html_tree = None

    def retrieve_html(self, url):
        response = requests.get(url)
        self._html_tree = html_to_json.convert(response.text)

    def get_html_tree(self):
        return self._html_tree

