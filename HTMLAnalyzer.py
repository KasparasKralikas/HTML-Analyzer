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
        html_tree = self.html_parser.get_html_tree()
        tags_frequency = {}
        self._get_most_comon_tag([html_tree], tags_frequency)
        most_common_tags = sorted(tags_frequency, key=tags_frequency.get, reverse=True)
        return most_common_tags[0]

    def get_longest_path(self):
        return None
    
    def get_longest_path_with_max_most_common_tag_occurences(self):
        return None

    def _get_unique_tags(self, html_tree, unique_tags: set):
        if type(html_tree) is list:
            for element in html_tree:
                if hasattr(element, 'keys'):
                    keys = element.keys()
                    for key in keys:
                        if key not in self.html_parser.RESERVED_TAGS:
                            unique_tags.add(key)
                            self._get_unique_tags(element[key], unique_tags)

    def _get_most_comon_tag(self, html_tree, tags_frequency: dict):
        if type(html_tree) is list:
            for element in html_tree:
                if hasattr(element, 'keys'):
                    keys = element.keys()
                    for key in keys:
                        if key not in self.html_parser.RESERVED_TAGS:
                            if key is not None:
                                nested_values_count = self._count_nested_values(element[key])
                                tag_frequency = 1 if nested_values_count == 0 else nested_values_count
                                if key in tags_frequency:
                                    tags_frequency[key] = tags_frequency[key] + tag_frequency
                                else:
                                    tags_frequency[key] = tag_frequency
                                self._get_most_comon_tag(element[key], tags_frequency)

    def _count_nested_values(self, html_tree):
        count = 0
        for element in html_tree:
            if hasattr(element, 'keys'):
                keys = element.keys()
                for key in keys:
                    if key in self.html_parser.VALUE_TAGS:
                        count = count + 1
        return count