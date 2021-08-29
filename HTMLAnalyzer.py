from HTMLParser import HTMLParser

class HTMLAnalyzer:
    def __init__(self, html_parser: HTMLParser):
        self.html_parser = html_parser
    
    def get_unique_tags(self):
        html_tree = self.html_parser.get_html_tree()
        unique_tags = set()
        self._get_unique_tags([html_tree], unique_tags)
        return unique_tags

    def get_most_common_tag(self):
        return None

    def get_longest_path(self):
        return None
    
    def get_longest_path_with_max_most_common_tag_occurences(self):
        return None

    def _get_unique_tags(self, html_tree, unique_tags: set):
        if type(html_tree) is list:
            for element in html_tree:
                keys = element.keys()
                for key in keys:
                    if key != '_value':
                        unique_tags.add(key)
                        self._get_unique_tags(element[key], unique_tags)
