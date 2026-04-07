from app.blueprints import blueprint
from app import db, models, forms
from flask import render_template, request, redirect, url_for, jsonify, flash, send_from_directory, current_app
from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone
from hashlib import md5
import os

# Default route of the application
@blueprint.route("/")
@login_required
def index():
    return render_template("home.html")

# Login route of the application
@blueprint.route("/login", methods=["GET", "POST"])
def login():
    # Ensure that the user cannot access this route if they are already signed in
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = forms.LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        # Retrieve the user from the database based on the provided username/email address
        username = form.username.data.lower().strip()
        password = form.password.data.strip()

        # Initialise the database
        sqlite = sqlite3.Connection("app/app.db")
        cursor = sqlite.cursor()

        # Retrieve the passwords for the signed in user and close the database
        user = cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'").fetchone()
        sqlite.close()

        # Ensure that the user exists and that the password hash matches
        if user is None:
            flash("The username and password do not match")
            return redirect(url_for('main.login'))

        # Log the user in
        user = db.session.scalar(sa.select(models.Users).where(models.Users.username == user[1]))
        login_user(user, remember=form.remember_user.data)

        return redirect(url_for('main.index'))
    return render_template("login.html", form=form) # Display login page

# Signup route of the application
@blueprint.route("/register", methods=["GET", "POST"])
def signup():
    # Ensure that the user cannot access this route if they are already signed in
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = forms.RegistrationForm()
    if request.method == "POST" and form.validate_on_submit():
        # Extract the information from the form
        username = form.username.data.strip()
        password = form.password.data.strip()

        # Create the user entry and add it to the database
        user = models.Users(
            username=username, 
            password=password
        )
        db.session.add(user)
        db.session.commit()

        # Log in the user and redirect them to the homepage
        login_user(user, remember=True)
        return redirect(url_for('main.index'))
    return render_template("register.html", form=form) # Display sign up page

@blueprint.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('main.index'))

@blueprint.route('/system/run', methods=["POST"])
def run():
    # Retrieve the parameters from the request
    text = request.args.get('text', default='')
    print(text)

    # Get the output from the command run (adapted from https://stackoverflow.com/questions/18739239/python-how-to-get-stdout-after-running-os-system)
    os.system(f"echo {text} > output.txt")
    if os.path.exists("output.txt"):
        with open("output.txt", "r") as file:
            output = file.read()
        os.remove("output.txt")

    return jsonify({"output": output})