from os import path, listdir, mkdir
from pathlib import Path
from markdown_to_html_node import markdown_to_html_node
from extractions.extract_title import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating pages from {from_path} to {dest_path} using {template_path}")
    
    markdown_path = from_path + '/index.md'
    
    with open(markdown_path, encoding='utf-8') as markdown:
        read_markdown = markdown.read()
    
    page_title = extract_title(read_markdown)
    markdown_html = markdown_to_html_node(read_markdown).to_html()
    
    with open(template_path, encoding='utf-8') as html_template:
        read_html = html_template.read()

    replace_title = read_html.replace("{{ Title }}", page_title)
    replace_html = replace_title.replace("{{ Content }}", markdown_html)
    
    new_path = ''
    if(path.basename(from_path) == 'content'):
        new_path = dest_path
    else:
        new_path = path.join(dest_path, path.basename(from_path))
    
    if(path.exists(new_path) == False):
        mkdir(new_path)
    
    new_html = open(new_path + '/index.html', 'x', -1, "utf-8",)
    new_html.write(replace_html)

def generate_page_recursive(from_path, template_path, dest_path):
    cur_path = listdir(from_path)

    for archive in cur_path:
        cur_dir_path = path.join(from_path, archive)
        
        if (path.isdir(cur_dir_path) and len(listdir(cur_dir_path)) > 0 and Path(archive) != Path('__pycache__')):
            generate_page_recursive(cur_dir_path, template_path, dest_path)            

        if(archive.endswith('.md')):
            generate_page(from_path, template_path, dest_path)
        
