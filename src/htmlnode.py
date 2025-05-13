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

