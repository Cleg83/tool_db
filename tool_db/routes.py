from flask import render_template, request, redirect, url_for, session
from tool_db import app, db
from tool_db.models import MainCategory, SubCategory, Tool, User, MyToolbox, MyVideos


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/categories")
def categories():
    main_categories = MainCategory.query.order_by(MainCategory.main_category_name).all()

    category_icons = {
        "Hand Tools": "fa-solid fa-hammer",
        "Power Tools": "fa-solid fa-plug-circle-bolt",
        "Machines": "fa-solid fa-gears",
        "Measuring & Marking": "fa-solid fa-ruler-horizontal",
        "Sharpening": "fa-solid fa-arrow-rotate-right",
        "Dust Extraction": "fa-solid fa-broom"
    }
    return render_template("categories.html", main_categories=main_categories, category_icons=category_icons)


@app.route("/add_category")
def add_category():
    return render_template("add_category.html")


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
        main_category = request.form.get("main_category")

        if not main_category:
            # Handle the case where main_category is missing
            flash("Main category is required.", "error")
            return redirect(url_for("add_sub_category"))

        # Ensure that main_category is converted to integer if it's not already
        try:
            main_category_id = int(main_category)
        except ValueError:
            flash("Invalid main category selected.", "error")
            return redirect(url_for("add_sub_category"))

        sub_category = SubCategory(sub_category_name=sub_category_name, main_category_id=main_category_id)
        db.session.add(sub_category)
        db.session.commit()
        return redirect(url_for("categories"))

    main_categories = MainCategory.query.all()
    return render_template("add_sub_category.html", main_categories=main_categories)


@app.route("/edit_sub_category/<int:sub_category_id>")
def edit_sub_category(sub_category_id):
    sub_category = SubCategory.query.get_or_404(sub_category_id)
    tools = Tool.query.filter_by(sub_category_id=sub_category_id).all()
    main_categories = MainCategory.query.order_by(MainCategory.main_category_name).all()
    return render_template("edit_sub_category.html", sub_category=sub_category, tools=tools, main_categories=main_categories)


@app.route("/selected_category/<category_name>.html")
def selected_category(category_name):
    main_category_name = category_name.replace("_", " ").title()
    main_category = MainCategory.query.filter_by(main_category_name=main_category_name).first()

    if main_category:
        sub_categories = SubCategory.query.filter_by(main_category_id=main_category.id).all()
        return render_template("selected_category.html", main_category=main_category, sub_categories=sub_categories)
    else:
        return render_template("404.html"), 404
    

@app.route("/selected_subcategory/<int:sub_category_id>.html")
def selected_subcategory(sub_category_id):
    sub_category = SubCategory.query.get_or_404(sub_category_id)
    tools = Tool.query.filter_by(sub_category_id=sub_category_id).all()
    return render_template("selected_subcategory.html", sub_category=sub_category, tools=tools)


@app.route("/add_tool", methods=["GET", "POST"])
def add_tool():
    main_categories = MainCategory.query.all()

    if request.method == "POST":
        step = request.form.get('step')

        if step == "1":
            # Store the tool details in session
            session["tool_name"] = request.form.get('tool_name')
            session["tool_description"] = request.form.get("tool_description")
            session["tool_videos"] = request.form.get("tool_videos")
            session["product_links"] = request.form.get("product_links")
            return render_template("add_tool_step2.html", main_categories=main_categories)
        
        elif step == "2":
            # Store the main category selection in session
            session["main_category_id"] = request.form.get("main_category")
            # Filter sub-categories based on main category
            subcategories = SubCategory.query.filter_by(main_category_id=session["main_category_id"]).all()
            return render_template("add_tool_step3.html", subcategories=subcategories)
        
        elif step == "3":
            # Store the sub-category selection in session
            sub_category_id = request.form.get("sub_category")

            # Create a new tool and save to the database
            new_tool = Tool(
                tool_name=session["tool_name"],
                tool_description=session["tool_description"],
                tool_videos=session["tool_videos"],
                tool_links=session["product_links"],
                main_category_id=session["main_category_id"],
                sub_category_id=sub_category_id
            )
            db.session.add(new_tool)
            db.session.commit()

            # Clear the session
            session.clear()

            return redirect(url_for("categories"))
    
    return render_template("add_tool_step1.html")


@app.route("/edit_tool")
def edit_tool():
    return render_template("edit_tool.html")


@app.route("/glossary")
def glossary():
    tools = Tool.query.order_by(Tool.tool_name).all()  # Fetch tools in alphabetical order
    return render_template("glossary.html", tools=tools)


@app.route("/tool/<int:tool_id>")
def tool(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    return render_template("tool.html", tool=tool)