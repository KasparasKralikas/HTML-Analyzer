from flask import Flask, request, jsonify
from HTMLParser import HTMLParser
from HTMLAnalyzer import HTMLAnalyzer
import time

PORT = 5000

app = Flask(__name__)


@app.route('/analyze', methods=['GET'])
def analyze_url():
    start_time = time.time()
    if 'url' not in request.args:
        return 'Missing required url query parameter', 400
    url = request.args.get('url')
    try:
        html_analyzer.html_parser.retrieve_html_tree_from_url(url)
        response = {
            'unique_tags': list(html_analyzer.get_unique_tags()),
            'most_common_tag': html_analyzer.get_most_common_tag(),
            'longest_path': html_analyzer.get_longest_path(),
            'longest_path_with_max_most_common_tag_occurences': html_analyzer.get_longest_path_with_max_most_common_tag_occurences(),
            'execution_time_in_seconds': round((time.time() - start_time), 3)
        }
        return jsonify(response)
    except:
        return 'Something went wrong on the server side', 500


if __name__ == '__main__':
    html_parser = HTMLParser()
    html_analyzer = HTMLAnalyzer(html_parser)
    app.run(port=PORT)
