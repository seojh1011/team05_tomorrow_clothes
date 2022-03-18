from django.contrib.auth.hashers import make_password
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from ninja import Router, Form
from user_admission.models import User

from user_admission.apis.v1.schemas.register_request import RegisterRequest
from user_admission.apis.v1.schemas.register_response import RegisterResponse
from user_admission.sevices.login_service import create_user


register = Router(tags=["MemberManagement"])


# register page render router
@register.get("/", response=RegisterResponse)
def get_register_page(request: HttpRequest) -> HttpResponse:
    return render(request, "register.html")

@register.post('/')
def insert_register(request, register_request: RegisterRequest = Form(...)):
    User.objects.create_user(nick_name=register_request.nick_name, username=register_request.username, password=register_request.password)
    return redirect("/login/")