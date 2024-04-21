class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is not None:
            props_string = ""
            
            for key, value in self.props.items():
                props_string += f' {key}="{value}"'
                
            return props_string
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None,props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError("Please provide a value.")
        if self.tag is None:
            return self.value
    
        props_string = self.props_to_html() if self.props is not None else ''
    
        return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("Please provide a tag.")
        if self.children is None:
            raise ValueError("Please provide a children.")    

        children_html = ''
        for node in self.children:
            children_html += node.to_html()
        
        props_string = self.props_to_html() if self.props is not None else ''
        return f"<{self.tag}{props_string}>{children_html}</{self.tag}>\n\n"
            
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
            
    