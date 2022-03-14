from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from ninja import Router

from user_admission.apis.v1.schemas.register_response import RegisterResponse
from user_admission.apis.v1.schemas.register_request import RegisterRequest

from user_admission.sevices.login_service import create_user


register = Router(tags=["MemberManagement"])


# register page render router
@register.get("/", response=RegisterResponse)
def get_register_page(request: HttpRequest) -> HttpResponse:
    return render(request, "register.html")


@register.post('/')
def insert_register(request, register_request: RegisterRequest ):
    create_user(username=register_request.username, password=register_request.password)
    return redirect("/login/")
