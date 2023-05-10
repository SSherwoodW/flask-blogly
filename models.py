from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"


def connect_db(app):
    db.app = app
    db.init_app(app)

class User (db.Model):
    """Site user"""

    __tablename__ = "users"

    def __repr__(self):
        """Show info about user."""
        u = self
        return f"<User id={u.id} first name={u.first_name} last name={u.last_name}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False)
    last_name = db.Column(db.String(50),
                     nullable=False)
    image_url = db.Column(db.Text,
                        nullable=True,
                        default=DEFAULT_IMAGE_URL)
    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

    @property
    def full_name(self):
        """Make full name of user"""
        return f"{self.first_name} {self.last_name}"

class Post (db.Model):
    """User post."""
    __tablename__ = "posts"


    def __repr__(self):
        return f"<Post {self.title} {self.content} {self.created_at} {self.user_id}>"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    title = db.Column(db.Text,
                      nullable=False)
    content = db.Column(db.Text,
                        nullable=False)
    created_at = db.Column(db.DateTime,
                           nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
