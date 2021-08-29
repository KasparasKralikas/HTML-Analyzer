import html_to_json
import requests

class HTMLParser:

    _html_tree = None

    RESERVED_TAGS = ['_value', '_values', '_attributes']

    def retrieve_html_tree_from_url(self, url):
        response = requests.get(url)
        self._html_tree = html_to_json.convert(response.text)

    def retrieve_html_tree_from_html_string(self, html_string):
        self._html_tree = html_to_json.convert(html_string)

    def get_html_tree(self):
        return self._html_tree

