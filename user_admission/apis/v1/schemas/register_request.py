from ninja import Schema


class RegisterRequest(Schema):
    nick_name: str
    username: str
    password: str

