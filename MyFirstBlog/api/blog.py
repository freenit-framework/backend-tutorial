from freenit.api.methodviews import MethodView
from flask_smorest import Blueprint

from ..schemas.blog import BlogSchema

blueprint = Blueprint('blogs', 'blogs')


@blueprint.route('', endpoint='blog')
class BlogListAPI(MethodView):
    @blueprint.response(BlogSchema)
    @blueprint.arguments(BlogSchema)
    def post(self, args):
        """Create blog post"""
        return args
