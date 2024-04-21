from markdown_to_blocks import markdown_to_blocks

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    header = blocks[0]
    header_tag = blocks[0].split()[0]
    
    if header_tag != '#': 
        raise Exception("All pages need a single h1 header.")
   
    header_text = header.split('#')[1].strip()
    return header_text
