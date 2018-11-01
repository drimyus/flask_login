import os
import math
import numpy as np
from flask import Flask, flash, render_template, request, redirect, url_for, send_from_directory
from forms import LoginForm

from db_utils import DBUtils


"""
*-------------------------------------------------------*
|                   Flask Sever Session                 |
*-------------------------------------------------------*
"""
# Initialize the Flask application
app = Flask(__name__)

# This is the path to the upload directory
app.config['CONTAINER'] = 'container'
app.config['file'] = 'app.zip'
app.config['SECRET_KEY'] = "cipherbook="


# Route that will process the file upload
@app.route('/', methods=['POST', 'GET'])
def login():
    login_form = LoginForm(request.form)
    if request.method == "POST":
        db = DBUtils()

        username = login_form.username.data
        password = login_form.password.data
        print(username, password)

        ret = db.check_users(username=username, password=password)
        if ret == 1:
            # download the zip file
            print("downloading")
            return send_from_directory(directory=app.config['CONTAINER'], filename=app.config['file'])
        elif ret == 0:
            error = 'Invalid credentials'

        elif ret == -1:
            error = "cannot connect to the DB"

        else:
            error = ""
        return render_template('login.html', error=error, login_form=login_form)

    return render_template('login.html', login_form=login_form, error=None)


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True,
        threaded=True,
    )
