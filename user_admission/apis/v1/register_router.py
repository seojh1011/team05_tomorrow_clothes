from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from ninja import Router, Form
from user_admission.models import User

from user_admission.apis.v1.schemas.register_request import RegisterRequest
from user_admission.apis.v1.schemas.register_response import RegisterResponse
from user_admission.sevices.login_service import create_user
#
# account = Router(tags=["MemberManagement"])

register = Router(tags=["MemberManagement"])

# register page render router
@register.get("/", response=RegisterResponse)
def get_register_page(request: HttpRequest) -> HttpResponse:
    return render(request, "register.html")

@register.post('/')
def insert_register(request, register_request: RegisterRequest = Form(...)):
    # password = make_password(register_request.password)
    # print('1')
    # print(register_request.nick_name)
    # print(register_request.username)
    # print(register_request.password)
    User.objects.create_user(nick_name=register_request.nick_name,
                username=register_request.username, password=register_request.password)
    # print('2')
    return redirect("/login/")

# register = Router(tags=["Register"])
#
# @register.post('/')
# def insert_register(request, register_request: RegisterRequest ):
#     create_user(username=register_request.username, password=register_request.password)
#     return redirect("/login/")
