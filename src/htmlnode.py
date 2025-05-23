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
        html = ""
        for prop, val in self.props.items():
            html += f"{prop}={val} "
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
        rep += "tag: "+self.tag
        rep += "\nvalue: "+self.value
        rep += "\nchildren: "+self.children
        rep += "\nprops: "+self.props_to_html()
        # for keys, vals in self:
        #     if isinstance(vals, dict):
        #         __repr__(vals)
        #     else:
        #         rep += vals
        return rep

# class LeafNode(HTMLNode):
#     def __init__(self, value, tag=None):
#         super().__init__(value, tag)