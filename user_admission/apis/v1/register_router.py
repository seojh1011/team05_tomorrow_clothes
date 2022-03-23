from typing import Dict

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from ninja import Form, Router

from user_admission.apis.v1.schemas.register_request import RegisterRequest
from user_admission.apis.v1.schemas.register_response import RegisterResponse
from user_admission.sevices.create_user_service import (
    create_user,
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
    user = create_user(
        register_request.email, register_request.password, register_request.nick_name
    )
    new_user_msg = str(list(user.keys()))
    if new_user_msg == "error":
        return redirect("/login")
    else:
        return render(request, "register.html")


@account.post("/reduplication")
def post_email_reduplication(request: HttpRequest, email: str) -> object:
    check = email_check(email)
    # print(type(check))
    return check


@account.post("/password")
def post_password_reduplication(request: HttpRequest, password: str) -> object:
    check = password_check(password)
    return check
