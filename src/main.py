from htmlnode import  HTMLNode, LeafNode, ParentNode
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from text_node_to_html import text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter
from extract import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_image, split_nodes_link


def main():
    text = 'This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)'
    
    
    def text_to_textnodes(text):    
        node = TextNode(text, text_type_text)
        
        bold_split = split_nodes_delimiter([node], '**', text_type_bold)
        italic_split = split_nodes_delimiter(bold_split, '*', text_type_italic)
        code_split = split_nodes_delimiter(italic_split, '`', text_type_code)
        image_split = split_nodes_image(code_split)
        link_split = split_nodes_link(image_split)
        
        return link_split
    
    print(text_to_textnodes(text))
    
main()