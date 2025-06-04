import re
def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    aux_blocks = []
    for block in blocks:
        if '\n' in block:
            splitted = re.split(r'\n( )*', block)
            if ' ' in splitted:
                splitted.pop(splitted.index(' '))
            print('SPLITTED', splitted)
            aux_blocks.append('\n'.join(splitted).strip())
            continue
        aux_blocks.append(block.strip('\n '))
        
    # for block in aux_blocks:
    #     if '\n' in block:
    #         splitted = re.split(r'\n( )*', block)
    #         if ' ' in splitted:
    #             splitted.pop(splitted.index(' '))
    #         print('SPLITTED', splitted)
    #         '\n'.join(splitted)
        
         

    print(aux_blocks)