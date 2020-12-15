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

@blueprint.route('/<slug>', endpoint='blog')
class BlogApi(MethodView):
    @blueprint.response(BlogSchema)
    def get(self, slug):
        """ Get blog details """
        try:
            blog = Blog.get(slug = slug)
        except Blog.DoesNotExist:
            abort(404, message='Blog not found')
        return blog

    @jwt_required
    @blueprint.response(BlogSchema)
    def delete(self, slug):
        """ Delete blog post """
        try:
            blog = Blog.get(slug = slug)
        except Blog.DoesNotExist:
            abort(404, message='Blog not found')
        blog.delete_instance()
        return blog

    @jwt_required
    @blueprint.arguments(BlogSchema(partial=True))
    @blueprint.response(BlogSchema)
    def patch(self, args, slug):
        """Edit blog post"""
        try:
            blog = Blog.get(slug = slug)
        except Blog.DoesNotExist:
            abort(404, message='Blog not found')
        for field in args:
            setattr(blog, field, args[field])
        blog.save()
        return blog
