from .settings import ma 
from .models import Post

class PostSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "author", "resume", "content", "image", "date"]


posts_schema = PostSchema(many=True)
post_schema = PostSchema()