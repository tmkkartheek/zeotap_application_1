import pytest
from backend.ast import ASTBuilder

def test_create_rule():
    builder = ASTBuilder()
    rule_string = "age > 30 AND department = 'Sales'"
    ast = builder.create_rule(rule_string)
    assert ast is not None

def test_evaluate_rule():
    builder = ASTBuilder()
    rule_string = "age > 30 AND department = 'Sales'"
    ast = builder.create_rule(rule_string)
    data = {"age": 35, "department": "Sales"}
    assert builder.evaluate_rule(ast, data) == True

if __name__ == "__main__":
    pytest.main()
