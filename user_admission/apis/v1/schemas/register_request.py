from ninja import Schema


class RegisterRequest(Schema):
    nick_name: str
    username: str = None
    email: str
    password: str
