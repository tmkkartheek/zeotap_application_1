from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Import the API routes after creating the app instance
from api.rule_engine_api import *

if __name__ == '__main__':
    app.run(debug=True)
