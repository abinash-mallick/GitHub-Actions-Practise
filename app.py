"""
This module provides functions for performing various arithmetic operations.
"""

from flask import Flask, render_template
from quotes import get_random_quote

app = Flask(__name__)

@app.route("/")
def home():
    """ Render the homepage with a random quote """
    quote = get_random_quote()
    return render_template("index.html", quote=quote)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
