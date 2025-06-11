import typing

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self): 
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        html = ""
        for prop, val in self.props.items():
            html += f'{prop}="{val}" '
        return html.strip()

    def __eq__(self, target):
        if not isinstance(target, HTMLNode):
            return NotImplemented

        return (self.props == target.props 
            and self.tag == target.tag
            and self.children == target.children
            and self.props == target.props
        )

    def __repr__(self):
        rep = ""
        if self.tag is not None:
            rep += "tag: "+self.tag
        if self.value is not None:
            rep += "\nvalue: "+self.value
        if self.children is not None:
            rep += f"\nchildren: {self.children}"
        if self.props is not None:
            rep += "\nprops: "+self.props_to_html()
        return rep

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        if children is not None:
            raise AttributeError("children are not allowed for LeafNodes")
        super().__init__(value=value, tag=tag, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Value cannot be empty")
        if self.tag is None or self.tag == "":
            return self.value
        render = f"<{self.tag} {self.props_to_html()}".strip()+">"
        render += f"{self.value}"
        render += f"</{self.tag}>"

        return render


class ParentNode(HTMLNode):
    def __init__(self, tag, children, value=None, props=None):
        if value is not None:
            raise AttributeError("Parent Nodes must not have values")
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is not defined")
        if self.children is None:
            raise ValueError("Parent Node must have children")
        
        node = f"<{self.tag} {self.props_to_html()}".strip()+">"
        for child in self.children:
            node += child.to_html()
        node += f"</{self.tag}>"
        return node
