"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy 


db = SQLAlchemy()

DEFAULT_IMAGE =  "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"




class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.text, nullable=False, default=DEFAULT_IMAGE)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")


    @property 
    def full_name(self):
        """full name of user"""
        return f"{self.first_name}  {self.last_name}"
    



def connect_db(app):
    """connect this to flask app """

    db.app = app
    db.init_app(app)

