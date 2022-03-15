from ninja import Schema


class RegisterRequest(Schema):
    username: str
    password: str

