from flask import render_template, request, redirect, url_for
from tool_db import app, db
from tool_db.models import MainCategory, SubCategory, Tool, User, MyToolbox, MyVideos


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/manage_categories")
def manage_categories():
    return render_template("manage_categories.html")


@app.route("/add_main_category", methods=["GET", "POST"])
def add_main_category():
    if request.method =="POST":
        main_category = MainCategory(main_category_name=request.form.get("main_category_name"))
        db.session.add(main_category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_main_category.html")


@app.route("/edit_main_category")
def edit_main_category():
    return render_template("edit_main_category.html")


@app.route("/add_sub_category")
def add_sub_category():
    return render_template("add_sub_category.html")


@app.route("/edit_sub_category")
def edit_sub_category():
    return render_template("edit_sub_category.html")


@app.route("/add_tool")
def add_tool():
    return render_template("add_tool.html")


@app.route("/edit_tool")
def edit_tool():
    return render_template("edit_tool.html")