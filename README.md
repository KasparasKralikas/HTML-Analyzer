# HTML Analyzer

Tool for simple HTML analysis with WEB API interface written in Python.

Given website url the tool provides:
- list of unique tags
- most common tag
- longest path starting from the root node
- longest path containing maximum occurences of the most common tag starting from the root node
- execution time in seconds for performance evaluation

### To launch locally:
Install requirements:
```
 pip install -r .\requirements.txt
```
```
python .\web_api.py
```

This will launch a flask web api on http://localhost:5000

### To use:
GET: http://localhost:5000/analyze?url=WEBSITE_URL

Requires url query parameter to be provided (url of the website to be analyzed)

Example response:
```
{
    "execution_time_in_seconds": 0.263,
    "longest_path": [
        "html",
        "body",
        "p",
        "span",
        "b"
    ],
    "longest_path_with_max_most_common_tag_occurences": [
        "html",
        "body",
        "p",
        "span",
        "b"
    ],
    "most_common_tag": "p",
    "unique_tags": [
        "body",
        "html",
        "span",
        "meta",
        "b",
        "h1",
        "p",
        "link",
        "script",
        "style",
        "title",
        "img",
        "head"
    ]
}
```

### To run unit tests for HTML_Analyzer class:
```
python -m unittest HTMLAnalyzerTests
```
Tests are located in *HTMLAnalyzerTests.py* script.

HTML examples for the tests are stored in *html_examples.py* script.

### Tips:
Launch locally and open any website to be analyzed. Then append http://localhost:5000/analyze?url= in front of the website url in the browser's address bar and go to the newly formed url to retrieve statistics (for example, http://localhost:5000/analyze?url=https://www.google.com).
