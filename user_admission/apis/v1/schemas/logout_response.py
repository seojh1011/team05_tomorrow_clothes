from ninja import Schema


class LogoutResponse(Schema):
    HttpResponse: str
