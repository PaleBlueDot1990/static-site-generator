class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value 
        self.children = children or []
        self.props = props or {}

    
    def to_html(self):
        raise NotImplementedError() 

        
    def props_to_html(self):
        html = ""
        for key, val in self.props.items():
            html += f" {key}=\"{val}\""
        return html 


    def __repr__(self):
        prettyNode = f"Tag: {self.tag} \n"
        prettyNode += f"Value: {self.value} \n"
        prettyNode += f"Number of Children: {len(self.children)} \n"
        prettyNode += f"Props: {self.props_to_html()} \n"
        return prettyNode



class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        
        if self.tag is None:
            return self.value
        
        prettyNode = ""
        if self.tag != "img":
            prettyNode += f"<{self.tag}{self.props_to_html()}>"
            prettyNode += self.value
            prettyNode += f"</{self.tag}>"
        else:
            prettyNode += f"<{self.tag}{self.props_to_html()}>"
        return prettyNode
        


class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)
    

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        
        if self.children is None:
            raise ValueError("Parent node must have a children")
        
        prettyNode = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            prettyNode += child.to_html()
        prettyNode += f"</{self.tag}>"
        return prettyNode

