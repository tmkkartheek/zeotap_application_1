from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

Base = declarative_base()

# Define a Rule model for storing rules in the database
class Rule(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    rule_data = Column(Text, nullable=False)  # Store the AST as a JSON string

# Initialize the database connection
engine = create_engine('sqlite:///rules.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create the rules table
def init_db():
    Base.metadata.create_all(engine)

# Save an AST rule to the database
def save_rule_to_db(rule_name, ast):
    try:
        # Convert AST to a JSON string
        ast_json = json.dumps(ast_to_dict(ast))
        new_rule = Rule(name=rule_name, rule_data=ast_json)
        session.add(new_rule)
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

# Load rules from the database
def load_rules_from_db():
    try:
        rules = session.query(Rule).all()
        return [
            {
                "id": rule.id,
                "name": rule.name,
                "rule_data": json.loads(rule.rule_data)  # Convert JSON string back to AST format
            }
            for rule in rules
        ]
    except Exception as e:
        raise e

# Helper function to convert AST Node to a dictionary for JSON serialization
def ast_to_dict(node):
    if node is None:
        return None
    return {
        'type': node.type,
        'value': node.value,
        'left': ast_to_dict(node.left),
        'right': ast_to_dict(node.right)
    }
