from freenit.schemas.base import BaseSchema
from freenit.schemas.user import BaseUserSchema as UserSchema
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
