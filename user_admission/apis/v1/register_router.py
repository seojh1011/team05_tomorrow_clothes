from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from ninja import Form, Router

from user_admission.apis.v1.schemas.register_request import RegisterRequest
from user_admission.apis.v1.schemas.register_response import RegisterResponse
from user_admission.sevices.login_service import create_user

# register = Router(tags=["MemberManagement"])
#                     # 스웨거에서 쓰는것

account = Router(tags=["MemberManagement"])


# register page render router
@account.get("/", url_name="register", response=RegisterResponse)
def get_register_page(request: HttpRequest) -> HttpResponse:
    return render(request, "register.html")


@account.post("/", url_name="register")
def insert_register(
    request: HttpRequest, register_request: RegisterRequest = Form(...)
) -> HttpResponse:
    create_user(
        username=register_request.username,
        email=register_request.email,
        nick_name=register_request.nick_name,
        password=register_request.password,
    )
    return redirect("test_1:login")
