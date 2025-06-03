import re

from textnode import TextNode, TextType
from extractor import extract_markdown_links, extract_markdown_images

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # print(old_nodes, delimiter, text_type)
    if delimiter == '':
        return old_nodes
    new_nodes = []
    for node in old_nodes:
        count = 0
        for char in node.text:
            if char == delimiter:
                count+=1

        if count % 2 == 1:
            raise Exception("Odd number of delimiters in text")
        if node.text_type is TextType.TEXT:
            if delimiter in node.text:
                new_list = node.text.split(delimiter)
                new_list_aux = []
                for idx, text in enumerate(new_list):
                    if not text and idx % 2 == 0:
                        continue
                    elif idx % 2 == 1:
                        new_list_aux.append(TextNode(text, text_type))
                    else:
                        new_list_aux.append(TextNode(text, TextType.TEXT))
                if new_list_aux:
                    new_nodes.extend(new_list_aux)
            elif node.text:
                new_nodes.append(TextNode(node.text, TextType.TEXT))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            links = extract_markdown_links(node.text)
            if links:
                current_index = 0
                for link in links:
                    print(link)
                    index = node.text.find(f"[{link[0]}]({link[1]})", current_index)
                    if node.text[current_index: index] != '':
                        new_nodes.append(TextNode(node.text[current_index:index], TextType.TEXT))
                    new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                    current_index = index + len(f"[{link[0]}]({link[1]})")
                if node.text[current_index: ] != '':
                    new_nodes.append(TextNode(node.text[current_index:], TextType.TEXT))
            else:
                new_nodes.append(node)
    print(new_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            images = extract_markdown_images(node.text)
            if images:
                current_index = 0
                for img in images:
                    index = node.text.find(f"![{img[0]}]({img[1]})", current_index)
                    if node.text[current_index: index] != '':
                        new_nodes.append(TextNode(node.text[current_index: index], TextType.TEXT))    
                    new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
                    current_index = index + len(f"![{img[0]}]({img[1]})")
                if node.text[current_index: ] != '':
                    new_nodes.append(TextNode(node.text[current_index:], TextType.TEXT))
            else:
                new_nodes.append(node)
    return new_nodes
