from HTMLParser import HTMLParser

def main():
    html_parser = HTMLParser()
    html_parser.retrieve_html_tree_from_url('https://pages.github.com/')
    print(html_parser.get_html_tree())
    return None

if __name__ == '__main__':
    main()