#!/usr/bin/python3
"""class Flask"""
from flask import Flask
"""class Flask"""


app = Flask(__name__)


# Define route for /airbnb-onepage/
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_airbnb():
    """
    Defines route for airbnb
    """
    return 'Hello, Airbnb!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
