from block_to_block_type import ( 
    block_type_paragraph,
    block_type_heading, 
    block_type_code,
    block_type_quote,
    block_type_unordered_list, 
    block_type_ordered_list,
    block_to_block_type
)

from text_to_text_nodes import text_to_textnodes
from text_node_to_html import text_node_to_html_node
from classes.htmlnode import LeafNode, ParentNode
from classes.textnode import TextNode
from markdown_to_blocks import markdown_to_blocks

def paragraph_to_html(block):
    paragraph_items = []
    
    text_nodes = text_to_textnodes(block)
    for node in text_nodes:
        text_html = text_node_to_html_node(node)
        paragraph_items.append(text_html)
    
    return ParentNode('p', paragraph_items)

def heading_to_html(block):
    heading_block = markdown_to_blocks(block)
    heading = heading_block[0].split()
    heading_length = len(heading[0])
    heading_text = heading_block[0].split("#" * heading_length)  
        
    heading_items = []
    text_nodes = text_to_textnodes(heading_text[1].lstrip())
    for node in text_nodes:
        text_html = text_node_to_html_node(node)
        heading_items.append(text_html)
    
    return ParentNode(f'h{heading_length}', heading_items)

def code_to_html(block):
    text_nodes = text_to_textnodes(block)
    code_text = text_nodes[0].text.lstrip()
    code_lines = text_node_to_html_node(TextNode(code_text, 'code'))
    return ParentNode('pre', [code_lines])

def quote_to_html(block):
    quote_lines = block.split('>')
    quotes = []
    
    for quote in quote_lines:
        if quote == '':
            continue
        quote_nodes = text_to_textnodes(quote.lstrip())
        
        for quote in quote_nodes:
            quote_html = text_node_to_html_node(quote)
            quotes.append(quote_html)
            
    return ParentNode('blockquote', quotes)

def unordered_to_html(block):
    unordered_list = markdown_to_blocks(block)[0].split('\n')
    unordered_list_items = []
    
    for i in range(len(unordered_list)):
        unordered_text = unordered_list[i].split('-', 1)[1]
        text_nodes = text_to_textnodes(unordered_text.strip())
        
        nodes = []
        for i in range(len(text_nodes)):
            text_html = text_node_to_html_node(text_nodes[i])
            nodes.append(text_html)
        unordered_list_items.append(ParentNode('li', nodes))
        
    return ParentNode('ul', unordered_list_items)

def ordered_to_html(block):
    ordered_list = markdown_to_blocks(block)[0].split('\n')
    ordered_list_items = []

    for i in range(len(ordered_list)):
        ordered_text = ordered_list[i].split(f'{i+1}.')[1]
        text_nodes = text_to_textnodes(ordered_text.strip())
        
        nodes = []
        for i in range(len(text_nodes)):
            text_html = text_node_to_html_node(text_nodes[i])
            nodes.append(text_html)
        ordered_list_items.append(ParentNode('li', nodes))
            
    return ParentNode('ol', ordered_list_items)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    list_of_nodes = []
    
    for block in blocks:
        if block_to_block_type(block) == block_type_heading:
            list_of_nodes.append(heading_to_html(block))

        if block_to_block_type(block) == block_type_code:
            list_of_nodes.append(code_to_html(block))
            
        if block_to_block_type(block) == block_type_quote:
            list_of_nodes.append(quote_to_html(block))
        
        if block_to_block_type(block) == block_type_ordered_list:
            list_of_nodes.append(ordered_to_html(block))

        if block_to_block_type(block) == block_type_unordered_list:
            list_of_nodes.append(unordered_to_html(block))
        
        if block_to_block_type(block) == block_type_paragraph:
            list_of_nodes.append(paragraph_to_html(block))

    return ParentNode('div', list_of_nodes)
