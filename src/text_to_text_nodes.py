from classes.textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from splitting.split_nodes_delimiter import split_nodes_delimiter
from splitting.split_nodes import split_nodes_image, split_nodes_link

def text_to_textnodes(text):    
    node = TextNode(text, text_type_text)
    
    image_split = split_nodes_image([node])
    link_split = split_nodes_link(image_split)
    bold_split = split_nodes_delimiter(link_split, '**', text_type_bold)
    italic_split = split_nodes_delimiter(bold_split, '_', text_type_italic)
    code_split = split_nodes_delimiter(italic_split, '`', text_type_code)
    
    return code_split
