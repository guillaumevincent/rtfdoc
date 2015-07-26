import CommonMark

parser = CommonMark.DocParser()
renderer = CommonMark.HTMLRenderer()


def transform_markdown_into_html(markdown_file_path):
    with open(markdown_file_path) as f:
        parsed_markdown = parser.parse(f.read())
        return renderer.render(parsed_markdown)
