from markdown_to_blocks import markdown_to_blocks
import re

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def block_to_block_type(markdown):
    block = markdown_to_blocks(markdown)
    block_split = block[0].split()
    block_type = block_split[0]    
    
    block_code = re.split(r'\w', block[0])
    code_start = block_code[0].split('\n')
    code_end = block_code[-1].split('\n')
    
    if('#' in block_type and len(block_type) <= 6):
        return block_type_heading
    
    if(code_start[0] == '```' and code_end[-1] == '```'):
        print
        return block_type_code
    
    if(block_type == '>' ):
        return block_type_quote
    
    if(block_type == '*' or block_type == '-'):
        return block_type_unordered_list
    
    if(block_type == '1.'):
        return block_type_ordered_list    
    
    return block_type_paragraph
