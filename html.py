def index_content():
    with open("index.html") as html_file:
        html_content = html_file.read()
        return html_content
