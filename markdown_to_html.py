import mistune
import re


def convert_markdown_to_html(markdown_file, output_file):
    # Read the markdown file
    with open(markdown_file, 'r') as file:
        markdown_content = file.read()

    # Convert the markdown to HTML with math support
    markdown_parser = mistune.Markdown(
        renderer=mistune.Renderer(escape=False, math=True))
    html_content = markdown_parser(markdown_content)

    # Replace $$math$$ with \( math \) for longer expressions
    html_content = re.sub(r'\$\$([\s\S]*?)\$\$', r'\\[\1\\]', html_content)

    # Replace $math$ with \( math \) for shorter expressions
    html_content = re.sub(r'(?<!\$)\$([^\$\n]+)\$', r'\(\1\)', html_content)


    # Write the HTML output to a file
    with open(output_file, 'w') as file:
        file.write(html_content)

# Provide the input and output file names
markdown_file = 'MLT.md'
output_file = 'mlt_pure_html.html'

# Convert the markdown to HTML
convert_markdown_to_html(markdown_file, output_file)
