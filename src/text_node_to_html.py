from classes.textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)

from classes.htmlnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)       
    
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)      
     
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)    
       
    if text_node.text_type == text_type_code:
        return LeafNode('code', text_node.text)
    
    if text_node.text_type == text_type_link:
        return LeafNode('a', text_node.text, {'href': text_node.url})
    
    if text_node.text_type == text_type_image:
        return LeafNode('img', '', {"src": text_node.url, "alt": text_node.text})
    
    raise Exception("Unsupported node type.")