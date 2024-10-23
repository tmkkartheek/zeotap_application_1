from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Rule Engine API. Use /create_rule to create a rule and /get_rules to retrieve rules."})

@app.route('/create_rule', methods=['POST'])
def create_rule():
    # Your implementation to create a rule
    return jsonify({"message": "Rule created"}), 201

@app.route('/get_rules', methods=['GET'])
def get_rules():
    # Your implementation to get rules
    return jsonify({"rules": []}), 200
