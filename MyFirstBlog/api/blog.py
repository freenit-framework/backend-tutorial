from freenit.api.methodviews import MethodView
from freenit.schemas.paging import PageInSchema, paginate
from flask_smorest import Blueprint, abort
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..schemas.blog import BlogSchema, BlogPageOutSchema
from ..models.blog import Blog
from ..models.user import User

blueprint = Blueprint('blogs', 'blogs')


@blueprint.route('', endpoint='blog')
class BlogListAPI(MethodView):
    @jwt_required
    @blueprint.response(BlogSchema)
    @blueprint.arguments(BlogSchema)
    def post(self, args):
        """Create blog post"""
        blog = Blog(**args)
        user_id = get_jwt_identity()
        print(user_id)
        try:
            user = User.get(id=user_id)
        except User.DoesNotExist:
            abort(404, message='User not found')
        blog.author = user
        blog.save()
        return blog

    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(BlogPageOutSchema)
    def get(self, pagination):
        """List blog posts"""
        query = Blog.select().order_by(Blog.author)
        return paginate(query, pagination)

