from ninja import Schema


class LoginRequest(Schema):
    username: str
    password: str
    csrfmiddlewaretoken:str
