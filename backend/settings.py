from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_cors import CORS
from flask_admin import Admin


BASE_DIR = Path(__file__).resolve().parent.parent

app = Flask(__name__, instance_path=BASE_DIR)
app.config["SECRET_KEY"] = "top-secret"

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{BASE_DIR}/db.sqlite3"
db = SQLAlchemy(app)

ma = Marshmallow(app)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173/*"}})



# URLConfig
from .import routes


# Admin Config
from .models import Post, Contact
from .admin import PostAdminView, ContactAdminView

admin = Admin(app, name="Admin", template_mode="bootstrap4")

admin.add_views(
    PostAdminView(Post, db.session),
    ContactAdminView(Contact, db.session)
)