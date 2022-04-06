from ninja import Schema


class RegisterRequest(Schema):
    nick_name: str
    email: str
    password: str

