from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import HttpResponse, render, redirect

from ninja import Router, Form
from django.contrib.auth.models import User
from django.contrib import auth


# from user_admission.apis.v1.schemas.login_request import LoginRequest
from user_admission.apis.v1.schemas.login_request import login_request
from user_admission.apis.v1.schemas.login_response import LoginResponse
from django.contrib import messages

account = Router(tags=["MemberManagement"])


# @account.get("/", response=LoginResponse)
# def get_login_page(request: HttpRequest) -> HttpResponse:
#     return render(request, "login.html")

# 경로가 ~ login/ 이고(/다음에 아무것도 없을때) get이면 위의 함수를 실행해라

@account.get("/", url_name='login', response=LoginResponse)
def get_login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")

@account.post("/", url_name='login', response=LoginResponse)
def post_login_page(request: HttpRequest) -> HttpResponse:
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(
        request, username=username, password=password
        )

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        return render(request, "login.html", {
            'error': 'Username or Password is incorrect.',
            })
    return render(request, "login.html")