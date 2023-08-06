from datetime import datetime
from slugify import slugify

from .settings import db 


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True)
    author = db.Column(db.String(100), nullable=False)
    resume = db.Column(db.Text(550), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    image = db.Column(db.Unicode(128))
    date = db.Column(db.DateTime(), default=datetime.utcnow())
    publish = db.Column(db.Boolean(), default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = ""

    def __str__(self):
        return self.title
    

class Contact(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime(), default=datetime.utcnow())

    def __str__(self):
        return self.name