from flask import render_template, request, redirect, url_for, session, flash, abort
from tool_db import app, db
from tool_db.models import MainCategory, SubCategory, Tool, User, MyToolbox
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

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    return render_template("add_category.html")


# Simple method for adding a main category
@app.route("/add_main_category", methods=["GET", "POST"])
def add_main_category():

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    if request.method =="POST":
        main_category = MainCategory(main_category_name=request.form.get("main_category_name"))
        db.session.add(main_category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_main_category.html")


@app.route("/edit_main_category/<int:category_id>", methods=["GET", "POST"])
def edit_main_category(category_id):

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    category = MainCategory.query.get_or_404(category_id)
    if request.method == "POST":
        category.main_category_name = request.form.get("main_category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_main_category.html", category=category)


@app.route("/delete_main_category/<int:category_id>")
def delete_main_category(category_id):

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    category = MainCategory.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_sub_category", methods=["GET", "POST"])
def add_sub_category():

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
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

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
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

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
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
        tools = Tool.query.filter_by(main_category_id=main_category.id).all()
        subcategories = Tool.query.filter_by(sub_category_id=Tool.sub_category_id).all()
        return render_template("selected_category.html", main_category=main_category, tools=tools, sub_categories=subcategories)
    else:
        # Handle case where main category doesn't exist
        flash("Category doesn't exist!", "error")
        return render_template("categories.html")
    

@app.route("/selected_subcategory/<int:subcategory_id>.html")
def selected_subcategory(subcategory_id):
    subcategory = SubCategory.query.get_or_404(subcategory_id)
    tools = Tool.query.filter_by(sub_category_id=subcategory.id).all()
    return render_template("selected_subcategory.html", subcategory=subcategory, tools=tools)


@app.route("/add_tool", methods=["GET", "POST"])
def add_tool():

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    main_categories = MainCategory.query.all()

    if request.method == "POST":
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
            # Filter subcategories by main category
            subcategories = SubCategory.query.filter_by(main_category_id=session["main_category_id"]).all()
            return render_template("add_tool_step3.html", subcategories=subcategories)
        
        elif step == "3":
            # Store subcategory selection in session
            sub_category_id = request.form.get("sub_category")

            # Convert comma-separated strings to lists
            tool_videos = [video.strip() for video in session.get("tool_videos", "").split(',') if video.strip()]
            product_links = [link.strip() for link in session.get("product_links", "").split(',') if link.strip()]

            # Create and save the new tool
            new_tool = Tool(
                tool_name=session["tool_name"],
                tool_description=session["tool_description"],
                tool_videos=tool_videos,
                tool_links=product_links,
                main_category_id=session["main_category_id"],
                sub_category_id=sub_category_id
            )
            db.session.add(new_tool)
            db.session.commit()

            # Clear the tool info from session
            session.pop("tool_name", None)
            session.pop("tool_description", None)
            session.pop("tool_videos", None)
            session.pop("product_links", None)
            session.pop("main_category_id", None)

            return redirect(url_for("categories"))
    
    return render_template("add_tool_step1.html")


@app.route("/edit_tool/<int:tool_id>", methods=["GET", "POST"])
def edit_tool(tool_id):

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    tool = Tool.query.get_or_404(tool_id)
    main_categories = MainCategory.query.all()

    if request.method == "POST":
        step = request.form.get('step')

        if step == "1":
            # Get and update session variables for the tool details
            session["tool_name"] = request.form.get('tool_name')
            session["tool_description"] = request.form.get("tool_description")
            
            # Convert comma-separated strings to lists and store in session
            session["tool_videos"] = [video.strip() for video in request.form.get("tool_videos", "").split(',') if video.strip()]
            session["product_links"] = [link.strip() for link in request.form.get("product_links", "").split(',') if link.strip()]

            return render_template("edit_tool_step2.html", tool=tool, main_categories=main_categories)
        
        elif step == "2":
            # Update the main category in session
            session["main_category_id"] = request.form.get("main_category")
            # Filter subcategories by main category
            subcategories = SubCategory.query.filter_by(main_category_id=session["main_category_id"]).all()
            return render_template("edit_tool_step3.html", tool=tool, subcategories=subcategories)
        
        elif step == "3":
            # Update the subcategory
            sub_category_id = request.form.get("sub_category")

            # Apply all updates to the tool object from session data
            tool.tool_name = session.get("tool_name")
            tool.tool_description = session.get("tool_description")
            tool.tool_videos = session.get("tool_videos")
            tool.tool_links = session.get("product_links")
            tool.main_category_id = session.get("main_category_id")
            tool.sub_category_id = sub_category_id

            # Commit the updates to the database
            db.session.commit()

            # Clear the session data for the tool
            session.pop("tool_name", None)
            session.pop("tool_description", None)
            session.pop("tool_videos", None)
            session.pop("product_links", None)
            session.pop("main_category_id", None)

            return redirect(url_for("selected_subcategory", subcategory_id=tool.sub_category_id))
        
    # Debugging output
    print(f"tool_videos (raw): {tool.tool_videos}, type: {type(tool.tool_videos)}")
    print(f"tool_links (raw): {tool.tool_links}, type: {type(tool.tool_links)}")
    
    # Displays links and videos as comma separated lists
    tool_videos = ",".join(tool.tool_videos or [])
    product_links = ",".join(tool.tool_links or [])

    # Debugging output after conversion
    print(f"tool_videos (converted): {tool_videos}")
    print(f"tool_links (converted): {product_links}")

    return render_template("edit_tool_step1.html", tool=tool, main_categories=main_categories, tool_videos=tool_videos, product_links=product_links)


@app.route("/delete_tool/<int:tool_id>")
def delete_tool(tool_id):

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    # Fetch tool to delete
    tool = Tool.query.get_or_404(tool_id)
    db.session.delete(tool)
    db.session.commit()
    # Fetch all tools to ensure glossary displays correctly when redirected
    tools = Tool.query.order_by(Tool.tool_name).all()
    return render_template("home.html", tools=tools)


@app.route("/manage_users")
def manage_users():

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))
    
    users = User.query.order_by(User.username).all()
    return render_template("manage_users.html", users=users)


@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):

    # Check if current user is admin
    if not session.get("role") == "admin":
        flash("Wind your neck in, you don't have permission to do that!", "error")
        return redirect(url_for("home"))

    # Fetch the user by ID
    user = User.query.get_or_404(user_id)

    # Delete the user
    db.session.delete(user)
    db.session.commit()

    flash(f"User {user.username} has been deleted.", "success")
    return redirect(url_for("manage_users"))


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
            session["user_id"] = user.id
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
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("login"))  # Redirect to login 


@app.route("/profile", methods=["GET"])
def profile():
    
    user_id = session.get("user_id")

    # Check if the user is logged in
    if user_id is None:
        flash("You need to be logged in to access that page!", "danger")
        return redirect(url_for("home"))  # Redirect to home page
    
    user = User.query.get_or_404(user_id)

    # Ensure the user is the one logged in
    if user_id != user.id:
        abort(403)

    return render_template("profile.html", user=user)


@app.route("/edit_username", methods=["GET", "POST"])
def edit_username():
    
    # Retrieves session user info
    user_id = session.get("user_id")

    # Check if the user is logged in
    if user_id is None:
        flash("You need to be logged in to access that page!", "danger")
        return redirect(url_for("home"))  # Redirect to home page
    
    user = User.query.get_or_404(user_id)

    # Ensure the user is the one logged in
    if user_id != user.id:
        abort(403)

    if request.method == "POST":
        new_username = request.form.get("edit_username")
        
        # Updates username
        if new_username:
            user.username = new_username
            db.session.commit()
            flash("Your username has been updated!", "success")
        else:
            flash("Username cannot be empty.", "danger")
        
        return redirect(url_for("profile"))

    return render_template("edit_username.html", user=user)


@app.route("/edit_password", methods=["GET", "POST"])
def edit_password():
    user_id = session.get("user_id")

    # Check if the user is logged in
    if user_id is None:
        flash("You need to be logged in to access that page!", "danger")
        return redirect(url_for("home"))  # Redirect to home page
    
    user = User.query.get_or_404(user_id)

    # Ensure the user is the one logged in
    if user_id != user.id:
        abort(403)

    if request.method == "POST":
        password = request.form.get("edit_password")
        password_confirm = request.form.get("edit_password_confirm")

        # Server-side validation
        if password != password_confirm:
            flash("Passwords do not match!", "error")
            return render_template("edit_password.html")

        # Hash the password
        hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

        # Update the user's password in the database
        user.password_hash = hashed_password
        db.session.commit()

        flash("Password updated successfully!", "success")
        return redirect(url_for("profile"))

    return render_template("edit_password.html")


@app.route("/delete_profile", methods=["POST"])
def delete_profile():

    user_id = session.get("user_id")

    # Check if the user is logged in
    if user_id is None:
        flash("You need to be logged in to access that page!", "danger")
        return redirect(url_for("home"))  # Redirect to home page
    
    user = User.query.get_or_404(user_id)

    # Ensure the user is the one logged in
    if user_id != user.id:
        abort(403)

    db.session.delete(user)
    db.session.commit()

    session.clear() # Clears session

    flash("Your profile has been deleted", "info")
    return redirect(url_for("home"))
    

@app.route("/my_toolbox")
def my_toolbox():

    user_id = session.get("user_id")

    # Check if the user is logged in
    if user_id is None:
        flash("You need to be logged in to access that page!", "danger")
        return redirect(url_for("home"))  # Redirect to home page
    
    user = User.query.get_or_404(user_id)

    # Ensure the user is the one logged in
    if user_id != user.id:
        abort(403)
    
    return render_template("my_toolbox.html")