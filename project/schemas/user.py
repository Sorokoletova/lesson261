from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    surname = fields.Str()
    password = fields.Str()
    email = fields.Str()
    favorite_genre = fields.Str()