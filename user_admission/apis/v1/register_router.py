import json
from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from ninja import Form, Router, Schema

from user_admission.apis.v1.schemas.register_request import RegisterRequest
from user_admission.apis.v1.schemas.register_response import RegisterResponse
from user_admission.sevices.create_user_service import (
    create_users,
    email_check,
    password_check,
)

# register = Router(tags=["MemberManagement"])
#                     # 스웨거에서 쓰는것

account = Router(tags=["MemberManagement"])


# register page render router
@account.get("/", url_name="register", response=RegisterResponse)
def get_register_page(request: HttpRequest) -> HttpResponse:
    return render(request, "register.html")


@account.post("/")
def create_user(
        request: HttpRequest, register_request: RegisterRequest = Form(...)
) -> HttpResponse:
    email = email_check(register_request.email)
    password = password_check(register_request.password)
    email = list(email.keys())[0]
    password = list(password.keys())[0]
    if email == 'success' and password == 'success':
        user = create_users(
            register_request.email, register_request.password, register_request.nick_name
        )
        new_user_msg = list(user.keys())[0]
        if new_user_msg == "error":
            return render(request, "register.html")
        else:
            return redirect("/login")
    else:
        return render(request, "register.html")


class Email(Schema):
    email: str



@account.post("/reduplication")
def post_email_reduplication(request: HttpRequest, email: Email):
    # print(asd)
    # print(email.email)
    # print(request.body)
    # email = json.loads(request.body)['email']

    check = email_check(email.email)
    # # print(type(check))
    return check



@account.post("/password")
def post_password_reduplication(request: HttpRequest) -> object:
    password = json.loads(request.body)['password']

    check = password_check(password)
    return check
