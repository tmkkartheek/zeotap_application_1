### 1. **How to Clone the Repository**
```bash
# Clone the repository
git clone https://github.com/tmkkartheek/zeotap_application_1.git
```

### 2. **Navigate to the Project Directory**
```bash
# Change to the project directory
cd zeotap_application_1
```

### 3. **Install Required Dependencies**
```bash
# Install dependencies using pip
pip install -r requirements.txt
```

### 4. **Initialize the Database**
```bash
# Initialize the SQLite database (run this once)
python -m backend.init_db
```

### 5. **Run the Flask Application**
```bash
# Start the Flask application
python app.py
```

### 6. **API Requests**

#### **Create a Rule**
Use Postman or curl to create a rule:
```bash
curl -X POST http://127.0.0.1:5000/create_rule -H "Content-Type: application/json" -d "{\"name\": \"test_rule\", \"rule\": \"(age > 30 AND department == 'Sales')\"}"
```

![image](https://github.com/user-attachments/assets/be5676bc-5b2c-45ff-a1ce-3934a1833b6c)


#### **Get Rules**
To retrieve all rules:
```bash
curl -X GET http://127.0.0.1:5000/get_rules
```

![image](https://github.com/user-attachments/assets/0a9258f6-985d-4bea-86be-2295def9b857)


### 7. **Push to GitHub**

Steps to push your project to GitHub:

```bash
# Initialize Git (if not done)
git init

# Add all files
git add .

# Commit the changes
git commit -m "Initial commit for rule engine application"

# Add remote origin
git remote add origin https://github.com/tmkkartheek/zeotap_application_1.git

# Push the changes to GitHub
git push -u origin main
```

### 8. **Security and Performance Considerations**
In the code, you can mention any placeholders or actual code snippets that help ensure the non-functional requirements like security, performance, and scalability. 

For example, you might want to mention input validation in your API methods:
```python
# Example of input validation in /create_rule
@app.route('/create_rule', methods=['POST'])
def create_rule():
    try:
        data = request.json
        rule_name = data.get('name')
        rule_string = data.get('rule')
        
        # Ensure both fields are provided
        if not rule_name or not rule_string:
            return {"error": "Rule name and rule string are required"}, 400

        # More validation logic can be added here for rule syntax
        ast = parse_rule_to_ast(rule_string)

        # Save the rule to the database
        save_rule_to_db(rule_name, rule_string, ast)

        return {"message": "Rule created successfully."}, 201
    except Exception as e:
        return {"error": str(e)}, 500
```
