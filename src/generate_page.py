from os import path
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    markdown_path = from_path + '/index.md'
    with open(markdown_path, encoding='utf-8') as markdown:
        read_markdown = markdown.read()
    
    page_title = extract_title(read_markdown)
    markdown_html = markdown_to_html_node(read_markdown).to_html()
    
    with open(template_path, encoding='utf-8') as html_template:
        read_html = html_template.read()

    replace_title = read_html.replace("{{ Title }}", page_title)
    replace_html = replace_title.replace("{{ Content }}", markdown_html)
    
    new_html = open(dest_path + '/index.html', 'x', -1, "utf-8",)
    new_html.write(replace_html)
 