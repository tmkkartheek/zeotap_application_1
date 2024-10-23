# backend/ast.py

class Node:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # Left child (Node)
        self.right = right  # Right child (Node)
        self.value = value  # Operand value (optional, for comparison)

    def evaluate(self, data):
        """Evaluates the AST against the provided user data."""
        if self.type == "operand":
            return self._evaluate_operand(data)
        elif self.type == "operator":
            return self._evaluate_operator(data)
    
    def _evaluate_operand(self, data):
        # Operand evaluation logic (e.g., "age > 30")
        attribute, operator, target_value = self.value
        user_value = data.get(attribute)

        if operator == '>':
            return user_value > target_value
        elif operator == '<':
            return user_value < target_value
        elif operator == '==':
            return user_value == target_value
        # Add more comparisons as needed

    def _evaluate_operator(self, data):
        # Operator evaluation (AND/OR)
        if self.value == 'AND':
            return self.left.evaluate(data) and self.right.evaluate(data)
        elif self.value == 'OR':
            return self.left.evaluate(data) or self.right.evaluate(data)


# Add the parse_rule_to_ast function
def parse_rule_to_ast(rule_string):
    """
    Parse the rule string into an Abstract Syntax Tree (AST).
    e.g., "age > 30 AND department == 'Sales'"
    """
    # Parse the rule string and create AST Nodes
    tokens = rule_string.split()
    # Here you can implement the parsing logic for operators/operands
    # This is a simplified version and can be expanded
    root = None

    for i in range(0, len(tokens), 4):  # Assuming each condition is separated by an operator
        operand = (tokens[i], tokens[i+1], tokens[i+2])  # (attribute, operator, value)
        if root is None:
            root = Node(type="operand", value=operand)
        else:
            operator = tokens[i+3]  # AND/OR
            root = Node(type="operator", left=root, right=Node(type="operand", value=operand), value=operator)
    
    return root


# Add the combine_rules function
def combine_rules(ast_list):
    """
    Combine multiple ASTs into a single AST using AND/OR logic.
    """
    if not ast_list:
        return None

    # Start by combining the first two ASTs
    combined_root = ast_list[0]

    for ast in ast_list[1:]:
        combined_root = Node(type="operator", left=combined_root, right=ast, value="AND")  # Example using AND

    return combined_root
