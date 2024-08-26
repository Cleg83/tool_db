from flask import render_template, request, redirect, url_for, session, flash
from tool_db import app, db
from tool_db.models import MainCategory, SubCategory, Tool, User, MyToolbox, MyVideos
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    tools = Tool.query.order_by(Tool.tool_name).all()
    return render_template("home.html", tools=tools)


@app.route("/categories")
def categories():
    # Fetch main categories and sort them alphabetically
    main_categories = MainCategory.query.order_by(MainCategory.main_category_name).all()

    # Icon dictionary (may be removed and replaced with icon field added to MainCategory model)
    category_icons = {
        "Hand Tools": "fa-solid fa-hammer",
        "Power Tools": "fa-solid fa-plug-circle-bolt",
        "Machines": "fa-solid fa-gears",
        "Measuring & Marking": "fa-solid fa-ruler-horizontal",
        "Sharpening": "fa-solid fa-arrow-rotate-right",
        "Dust Extraction": "fa-solid fa-broom"
    }
    # Pass variables to template
    return render_template("categories.html", main_categories=main_categories, category_icons=category_icons)


@app.route("/add_category")
def add_category():
    return render_template("add_category.html")


# Simple method for adding a main category
@app.route("/add_main_category", methods=["GET", "POST"])
def add_main_category():
    if request.method =="POST":
        main_category = MainCategory(main_category_name=request.form.get("main_category_name"))
        db.session.add(main_category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_main_category.html")


@app.route("/edit_main_category/<int:category_id>", methods=["GET", "POST"])
def edit_main_category(category_id):
    category = MainCategory.query.get_or_404(category_id)
    if request.method == "POST":
        category.main_category_name = request.form.get("main_category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_main_category.html", category=category)


@app.route("/delete_main_category/<int:category_id>")
def delete_main_category(category_id):
    category = MainCategory.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


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

        # Calls SubCategory method passing variables delcared above
        sub_category = SubCategory(sub_category_name=sub_category_name, main_category_id=main_category_id)
        db.session.add(sub_category)
        db.session.commit()
        return redirect(url_for("categories"))

    main_categories = MainCategory.query.all()
    return render_template("add_sub_category.html", main_categories=main_categories)


@app.route("/edit_sub_category/<int:subcategory_id>", methods=["GET", "POST"])
def edit_sub_category(subcategory_id):
    subcategory = SubCategory.query.get_or_404(subcategory_id)
    main_categories = MainCategory.query.order_by(MainCategory.main_category_name).all()
    # Fetches tool belonging to subcategory using sub_category_id
    tools = Tool.query.filter_by(sub_category_id=subcategory_id).all()

    if request.method == "POST":
        # Update the subcategory name
        subcategory.sub_category_name = request.form.get("subcategory_name")

        # Retrieve the selected main category ID from the form
        main_category_id = request.form.get("main_category")
        
        # Find the corresponding MainCategory instance
        main_category = MainCategory.query.get(main_category_id)

        if main_category:
            # Update the subcategory's main category
            subcategory.main_category = main_category

        db.session.commit()
        return redirect(url_for("categories"))

    return render_template("edit_sub_category.html", subcategory=subcategory, tools=tools, main_categories=main_categories)



@app.route("/delete_sub_category/<int:subcategory_id>")
def delete_sub_category(subcategory_id):
    subcategory = SubCategory.query.get_or_404(subcategory_id)
    db.session.delete(subcategory)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/selected_category/<category_name>.html")
def selected_category(category_name):
    main_category_name = category_name.replace("_", " ").title()
    main_category = MainCategory.query.filter_by(main_category_name=main_category_name).first()

    # Check if main category exists in db
    if main_category:
        subcategories = SubCategory.query.filter_by(main_category_id=main_category.id).all()
        return render_template("selected_category.html", main_category=main_category, sub_categories=subcategories)
    else:
        # Handle case where main category doesn't exist
        return render_template("404.html"), 404
    

@app.route("/selected_subcategory/<int:subcategory_id>.html")
def selected_subcategory(subcategory_id):
    subcategory = SubCategory.query.get_or_404(subcategory_id)
    tools = Tool.query.filter_by(sub_category_id=subcategory.id).all()
    return render_template("selected_subcategory.html", subcategory=subcategory, tools=tools)


@app.route("/add_tool", methods=["GET", "POST"])
def add_tool():
    main_categories = MainCategory.query.all()

    if request.method == "POST":
        # Fetches name="step" input element from add_tool templates which allows
        # splitting of add_tool into 3 steps
        step = request.form.get('step')

        if step == "1":
            # Store tool details in session
            session["tool_name"] = request.form.get('tool_name')
            session["tool_description"] = request.form.get("tool_description")
            session["tool_videos"] = request.form.get("tool_videos")
            session["product_links"] = request.form.get("product_links")
            return render_template("add_tool_step2.html", main_categories=main_categories)
        
        elif step == "2":
            # Store main category selection in session
            session["main_category_id"] = request.form.get("main_category")
            # Filter subcategories by main category to only show relevant subcategories in step 3
            subcategories = SubCategory.query.filter_by(main_category_id=session["main_category_id"]).all()
            return render_template("add_tool_step3.html", subcategories=subcategories)
        
        elif step == "3":
            # Store subcategory selection in session
            sub_category_id = request.form.get("sub_category")

            # Create new tool and save to db
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

            # Clear the tool info from session but keep admin logged in
            session.pop("tool_name", None)
            session.pop("tool_description", None)
            session.pop("tool_videos", None)
            session.pop("product_links", None)
            session.pop("main_category_id", None)

            return redirect(url_for("categories"))
    
    return render_template("add_tool_step1.html")


# TO FIX - The edit_tool is not working correctly - it is not displaying main or subcategories
@app.route("/edit_tool/<int:tool_id>", methods=["GET", "POST"])
def edit_tool(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    main_categories = MainCategory.query.all()

    if request.method == "POST":
        step = request.form.get('step')

        if step == "1":
            # Update the tool details
            tool.tool_name = request.form.get('tool_name')
            tool.tool_description = request.form.get("tool_description")
            tool.tool_videos = request.form.get("tool_videos")
            tool.tool_links = request.form.get("product_links")
            return render_template("edit_tool_step2.html", tool=tool, main_categories=main_categories)
        
        elif step == "2":
            # Update the main category
            main_category_id = request.form.get("main_category")
            tool.main_category_id = main_category_id
            # Filter subcategories by main category to only show relevant subcategories in step 3
            subcategories = SubCategory.query.filter_by(main_category_id=main_category_id).all()
            return render_template("edit_tool_step3.html", tool=tool, subcategories=subcategories)
        
        elif step == "3":
            # Update the subcategory
            tool.sub_category_id = request.form.get("sub_category")

            # Commit the updates to the database
            db.session.commit()

            return redirect(url_for("selected_subcategory", subcategory_id=tool.sub_category_id))
    
    return render_template("edit_tool_step1.html", tool=tool, main_categories=main_categories)


@app.route("/delete_tool/<int:tool_id>")
def delete_tool(tool_id):
    # Fetch tool to delete
    tool = Tool.query.get_or_404(tool_id)
    db.session.delete(tool)
    db.session.commit()
    # Fetch all tools to ensure glossary displays correctly when redirected
    tools = Tool.query.order_by(Tool.tool_name).all()
    return render_template("home.html", tools=tools)


@app.route("/glossary")
def glossary():
    tools = Tool.query.order_by(Tool.tool_name).all()
    return render_template("glossary.html", tools=tools)


@app.route("/tool/<int:tool_id>")
def tool(tool_id):
    tool = Tool.query.get_or_404(tool_id)
    return render_template("tool.html", tool=tool)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password_confirm = request.form.get("password_confirm")

        # Server-side validation
        if password != password_confirm:
            flash("Passwords do not match!", "error")
            return render_template("register.html")

        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "error")
            return render_template("register.html")

        # Hash the password
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        # Create a new user
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            session["username"] = username
            session["role"] = "admin" if username == 'admin' else 'user'
            flash(f"Logged in as {username}", "success")
            if session.get("role") == "admin":
                return redirect(url_for('categories'))
            else:
                return redirect(url_for('home'))  # Redirect to home page (will change to profile page in future)
        else:
            flash("Login failed. Check your username and/or password.", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)  # Remove username from session
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))  # Redirect to login or another page