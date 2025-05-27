from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # print(old_nodes, delimiter, text_type)
    new_nodes = []
    for node in old_nodes:
        # print("NODE", node)
        count = 0
        for c in node.text:
            if c == delimiter:
                count += 1
        
        if count % 2 != 0:
            raise Exception(f"unclosed delimiter {delimiter} detected. expected:{count + 1}, got: {count}")
        
        if node.text_type is TextType.TEXT:
            new_nodes.append(node)
            continue
        splits = node.text.split(delimiter)
        # print(node.text)
        for idx, split in enumerate(splits):
            # print("SPLIT:", split, "index:", idx)
            if idx % 2 == 1:
                match delimiter:
                    case ('`'):
                        new_nodes.append(TextNode(split, text_type=TextType.CODE))
                    case ('_'):
                        new_nodes.append(TextNode(split, text_type=TextType.ITALIC))
                    case ('**'):
                        new_nodes.append(TextNode(split, text_type=TextType.BOLD))
                    case _:
                        new_nodes.append(TextNode(split, text_type=TextType.TEXT))
            else:
                new_nodes.append(TextNode(split, text_type=TextType.TEXT))
    # print(new_nodes)
    return new_nodes