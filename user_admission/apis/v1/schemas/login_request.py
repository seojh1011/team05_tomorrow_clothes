# from ninja import Schema
#
#
# class LoginRequest(Schema):
#     username: str
#     password: str
from ninja.orm import create_schema

from user_admission.models import User

login_request = create_schema(User, fields=["username", "password"])
