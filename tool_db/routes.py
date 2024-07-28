from flask import render_template
from tool_db import app, db


@app.route("/")
def home():
    return render_template("home.html")