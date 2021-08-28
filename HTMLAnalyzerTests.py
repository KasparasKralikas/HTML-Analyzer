import unittest
from HTMLParser import HTMLParser
from HTMLAnalyzer import HTMLAnalyzer
from html_examples import HTML_EXAMPLE_1, HTML_EXAMPLE_2

class HTMLAnalyzerTests(unittest.TestCase):

    def test_get_unique_tags_from_valid_html(self):
        html_parser = HTMLParser()
        html_parser.retrieve_html_tree_from_html_string(HTML_EXAMPLE_2)
        html_analyzer = HTMLAnalyzer(html_parser)
        unique_tags = html_analyzer.get_unique_tags()
        expected_unique_tags = ['html', 'body', 'h1', 'p']
        self.assertListEqual(expected_unique_tags,  unique_tags)

    def test_get_most_common_tag_from_valid_html(self):
        html_parser = HTMLParser()
        html_parser.retrieve_html_tree_from_html_string(HTML_EXAMPLE_1)
        html_analyzer = HTMLAnalyzer(html_parser)
        most_common_tag = html_analyzer.get_most_common_tag()
        self.assertEqual('td', most_common_tag)

    def test_get_longest_path_from_valid_html(self):
        html_parser = HTMLParser()
        html_parser.retrieve_html_tree_from_html_string(HTML_EXAMPLE_2)
        html_analyzer = HTMLAnalyzer(html_parser)
        longest_path = html_analyzer.get_longest_path()
        self.assertEqual('html > body > table >tr > th', longest_path)

    def test_get_get_longest_path_with_max_most_common_tag_occurences_from_valid_html(self):
        html_parser = HTMLParser()
        html_parser.retrieve_html_tree_from_html_string(HTML_EXAMPLE_1)
        html_analyzer = HTMLAnalyzer(html_parser)
        longest_path = html_analyzer.get_longest_path_with_max_most_common_tag_occurences()
        self.assertEqual('html > body > table >tr > td', longest_path)

if __name__ == '__main__':
    unittest.main()