import sys

from freenit.schemas.base import BaseSchema
from freenit.schemas.user import BaseUserSchema as UserSchema
from freenit.schemas.paging import PageOutSchema
from marshmallow import fields


class BlogSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    title = fields.String(description='Title')
    author = fields.Nested(UserSchema, dump_only=True)
    content = fields.String(description='Content')
    date = fields.DateTime(
        description='Time when blog was created',
        dump_only=True,
    )
    slug = fields.String(description='Slug', dump_only=True)
    published = fields.Boolean(description='Published', default=False)
    image = fields.Url(description='Image Url')

PageOutSchema(BlogSchema, sys.modules[__name__])
