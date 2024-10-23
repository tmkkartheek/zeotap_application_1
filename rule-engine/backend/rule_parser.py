class Node:
    def __init__(self, node_type, value=None, left=None, right=None):
        self.type = node_type  # "operator" or "operand"
        self.value = value      # Value for operand nodes
        self.left = left        # Left child (for operators)
        self.right = right      # Right child (for operators)

    def to_dict(self):
        """Convert the Node object to a dictionary."""
        return {
            "type": self.type,
            "value": self.value,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
        }

def parse_rule_to_ast(rule_string):
    # Basic parsing logic (you may need to implement a more robust parser)
    tokens = rule_string.replace("(", " ( ").replace(")", " ) ").split()
    return parse_tokens(tokens)

def parse_tokens(tokens):
    if not tokens:
        raise SyntaxError("Empty rule")

    token = tokens.pop(0)

    if token == "(":
        left = parse_tokens(tokens)
        operator = tokens.pop(0)
        right = parse_tokens(tokens)
        tokens.pop(0)  # Remove the closing parenthesis
        return Node("operator", operator, left, right)
    elif token.isdigit() or token.replace(".", "", 1).isdigit():
        return Node("operand", float(token))
    else:
        return Node("operand", token)
