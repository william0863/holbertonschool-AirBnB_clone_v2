#!/usr/bin/python3
"""
Write a script that starts a Flask web application:

    Your web application must be listening on 0.0.0.0, port 5000
    You must use storage for fetching data from the storage engine
    (FileStorage or DBStorage) => from models import storage and storage.all
    After each request you must remove the current SQLAlchemy Session:
        Declare a method to handle @app.teardown_appcontext
        Call in this method storage.close()
    Routes:
        /states_list: display a HTML page: (inside the tag BODY)
            H1 tag: “States”
            UL tag: with the list of all State objects present in
            DBStorage sorted by name (A->Z) tip
                LI tag: description of one State: <state.id>:
                <B><state.name></B>
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
    app.run(host='0.0.0.0', port=5000)
