import sys
import markdown


def markdown_to_html(command):
    if sys.argv[1] == "markdown":
        with open(sys.argv[2], 'r') as file:
            content = file.read()
        with open(sys.argv[3], 'w') as f:
            f.write(markdown.markdown(content))

markdown_to_html(sys.argv[1])
