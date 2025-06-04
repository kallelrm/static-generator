import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"     


def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    aux_blocks = []
    for block in blocks:
        if '\n' in block:
            splitted = re.split(r'\n( )*', block)
            if ' ' in splitted:
                splitted.pop(splitted.index(' '))
            aux_blocks.append('\n'.join(splitted).strip())
            continue
        aux_blocks.append(block.strip('\n '))

    return aux_blocks

def block_to_blocktype(markdown):
    stripped = markdown.strip()

    if re.match(r'^#{1,6} ', markdown):
        return BlockType.HEADING
    if markdown.startswith('```') and markdown.endswith('```'):
        return BlockType.CODE
    if re.match(r'^(\n?>)', markdown, flags=re.MULTILINE):
        return BlockType.QUOTE
    if re.match(r'^(\n?-)', markdown, flags=re.MULTILINE):
        return BlockType.UNORDERED
    if re.match(r'^(\n?\d+\.)', markdown, flags=re.MULTILINE):
        return BlockType.ORDERED
    return BlockType.PARAGRAPH

def markdown_to_html(markdown):
    pass