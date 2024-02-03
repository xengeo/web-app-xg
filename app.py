import os
from flask import Flask, render_template, redirect
from lib.database_connection import get_flask_database_connection


app = Flask(__name__)






# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

@app.route('/', methods=['GET'])
def get_app_index():
    return render_template('index.html')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))