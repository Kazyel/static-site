def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')   
    list_of_blocks = []
    
    for block in blocks:
        if block == '':
            continue
        block = block.strip()
        list_of_blocks.append(block)
    
    return list_of_blocks
