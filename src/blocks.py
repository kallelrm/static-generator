import re
from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode
from textnode import TextNode, TextType
from splitter import *

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED = "unordered_list"
    ORDERED = "ordered_list"     

def markdown_to_blocks(markdown):
    markdown = markdown.strip()
    lines = markdown.split('\n')
    
    blocks = []
    current_block = []
    
    for line in lines:
        if line.strip() == '':
            if current_block:  
                blocks.append('\n'.join(current_block))
                current_block = []
        else:
            current_block.append(line.strip())
    
    if current_block:
        blocks.append('\n'.join(current_block))
    
    clean_blocks = []
    for block in blocks:
        stripped = block.strip()
        if stripped:
            clean_blocks.append(stripped)
    
    return clean_blocks


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

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    nodes = []
    for block in blocks:
        block_type = block_to_blocktype(block)
        match block_type:
            case BlockType.PARAGRAPH:
                paragraph = text_to_children(block)
                nodes.append(paragraph) 
            case BlockType.HEADING:
                header = text_to_header(block)
                nodes.append(header)
            case BlockType.QUOTE:
                quote = text_to_quote(block)
                nodes.append(quote)
            case BlockType.UNORDERED | BlockType.ORDERED:
                unordered = text_to_list(block, block_type)
                nodes.append(unordered)
            case BlockType.CODE:
                code = text_to_code(block)
                nodes.append(code)
    
    return ParentNode("div", children=nodes)

def text_to_children(md, context=False):
    lines = md.split('\n')
    cleaned_lines = [line.strip() for line in lines]
    text = ' '.join(cleaned_lines)
    text = re.sub(r'\s+', ' ', text).strip()

    text_nodes = text_to_textnodes(text)
    html_children = [text_node.text_to_html_node() for text_node in text_nodes]
    if context:
        return html_children
    p_node = ParentNode("p", children=html_children)

    return p_node


def text_to_header(md):
    count = 0
    for char in md:
        if char == "#":
            count+=1
        else:
            break
    # if md[count] != " ":
    #     return text_to_children(md)
    
    content = text_to_children(md[count:], True)

    p_node = ParentNode(f"h{count}", children=content)
    return p_node

def text_to_quote(md):
    lines = [text.strip() for text in re.split(r'\n? *>', md)[1:]]

    aux_index = 0
    quote_lines = []
    for index, value in enumerate(lines):
        if value == '':
            quote_lines.append(" ".join(lines[aux_index: index]))
            aux_index = index + 1
    
    quote_lines.append(" ".join(lines[aux_index:]))
    
    children = []
    for line in quote_lines:
        if line.strip():
            child = text_to_children(line)
            children.append(child)
    
    p_node = ParentNode("blockquote", children=children)
    return p_node


def text_to_list(md, blocktype):
    if blocktype == BlockType.UNORDERED:
        lines = md.split("- ")[1:] 
    else:
        lines = re.split(r"\d+\.\s+", md)[1:]

    children = []
    for line in lines:
        if line.strip():
            inline_content = text_to_children(line.strip(), True)
            li_node = ParentNode("li", inline_content)
            children.append(li_node)

    if blocktype == BlockType.UNORDERED:
        return ParentNode("ul", children)
    else:
        return ParentNode("ol", children)


def text_to_code(md):
    lines = md.splitlines()
    code_text = "\n".join(lines[1:-1]).rstrip()
    code_node = LeafNode("code", code_text)
    return ParentNode("pre", [code_node])
