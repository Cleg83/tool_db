from flask import render_template, request, redirect, url_for
from tool_db import app, db
from tool_db.models import MainCategory, SubCategory, Tool, User, MyToolbox, MyVideos


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categories")
def categories():
    main_categories = list(MainCategory.query.order_by(MainCategory.main_category_name).all())
    return render_template("categories.html", main_categories=main_categories)


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


@app.route("/add_sub_category", methods=["GET", "POST"])
def add_sub_category():
    if request.method == "POST":
        sub_category_name = request.form.get("sub_category_name")
        main_category_id = request.form.get("main_category_id")
        sub_category = SubCategory(sub_category_name=sub_category_name, main_category_id=main_category_id)
        db.session.add(sub_category)
        db.session.commit()
        return redirect(url_for("categories"))
    
    main_categories = MainCategory.query.all()
    return render_template("add_sub_category.html", main_categories=main_categories)


@app.route("/edit_sub_category")
def edit_sub_category():
    return render_template("edit_sub_category.html")


@app.route('/category_page/<category_name>.html')
def category_page(category_name):
    # Fetch the main category by name
    main_category = MainCategory.query.filter_by(main_category_name=category_name.replace('_', ' ').title()).first()
    if main_category:
        sub_categories = SubCategory.query.filter_by(main_category_id=main_category.id).all()
        return render_template('category_page.html', category_name=category_name, sub_categories=sub_categories)
    else:
        # Handle case where category is not found
        return render_template('404.html'), 404


@app.route("/add_tool")
def add_tool():
    return render_template("add_tool.html")


@app.route("/edit_tool")
def edit_tool():
    return render_template("edit_tool.html")