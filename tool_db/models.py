from tool_db import db
from sqlalchemy import Text
from werkzeug.security import generate_password_hash, check_password_hash


# main category model
class MainCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_category_name = db.Column(db.String(100), unique=True, nullable=False)
    sub_cats = db.relationship("SubCategory", backref="main_category",
                               cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"{self.main_category_name}"


# subcategory model
class SubCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sub_category_name = db.Column(db.String(100), unique=True, nullable=False)
    main_category_id = db.Column(db.Integer, db.ForeignKey("main_category.id",
                                 ondelete="CASCADE"), nullable=False)
    tools = db.relationship("Tool", backref="sub_category_ref",
                            cascade="all, delete", lazy=True)

    def __repr__(self):
        return f"{self.sub_category_name}"


# tool model
class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tool_name = db.Column(db.String(50), unique=True, nullable=False)
    tool_description = db.Column(Text, nullable=False)
    tool_videos = db.Column(db.JSON, nullable=True)
    tool_links = db.Column(db.JSON, nullable=True)
    main_category_id = db.Column(db.Integer, db.ForeignKey("main_category.id",
                                 ondelete="CASCADE"), nullable=False)
    sub_category_id = db.Column(db.Integer, db.ForeignKey("sub_category.id",
                                ondelete="CASCADE"), nullable=False)

    sub_category = db.relationship("SubCategory", backref="related_tools")
    toolbox_entries = db.relationship("MyToolbox", backref="tool_entries",
                                      cascade='all, delete', lazy=True)

    def __repr__(self):
        return "Name: {0} | Sub-Category: {1}".format(
            self.tool_name, self.sub_category_id
        )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    toolbox_items = db.relationship("MyToolbox", backref="user_toolbox_items",
                                    cascade="all, delete", lazy=True)

    def set_password(self, password):
        # Hashes the password
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        # Checks the password against the stored hash.
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"{self.username}"


# my toolbox model (where users can save their favourite tools
class MyToolbox(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id",
                        ondelete="CASCADE"), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey("tool.id",
                        ondelete="CASCADE"), nullable=False)

    user = db.relationship("User", backref="my_toolbox_items", lazy=True)
    tool = db.relationship("Tool", backref="my_toolbox_entries", lazy=True)

    def __repr__(self):
        return f"MyToolbox: User {self.user_id} | Tool {self.tool_id}"
