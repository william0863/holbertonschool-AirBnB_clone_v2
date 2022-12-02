#!/usr/bin/python3
"""
    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

# display the HTML page
@app.route('/states_list', strict_slashes=False)
def states():
    """access File/DB Storage for all State objects and render to HTML"""

    return render_template('7-states_list.html',
                           states=[st for st in storage.all('State').values()])

# rm SQL Alchemy Session
@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
