from flask import request, jsonify
from flask_restful import Resource

from .settings import api, db
from .models import Post, Contact
from .serializers import posts_schema, post_schema


class PostListView(Resource):
    def get(self):
        posts = Post.query.filter_by(publish=True)
        return posts_schema.dump(posts), 200
    

class PostDetailView(Resource):
    def get(self, post_slug):
        post = Post.query.filter_by(slug=post_slug).first()
        return post_schema.dump(post), 200
    
class ContactView(Resource):
    def post(self):
        data = request.get_json()
        new_contact = Contact(
            name=data["name"],
            email=data["email"],
            message=data["message"]
        )
        db.session.add(new_contact)
        db.session.commit()
        return jsonify({"message": "Votre message a été envoyé avec succès."})
       

api.add_resource(PostListView, "/api/posts")
api.add_resource(PostDetailView, "/api/posts/<string:post_slug>")
api.add_resource(ContactView, "/api/contact")