from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import HttpResponse, render, redirect
from ninja import Router, Form

# from user_admission.apis.v1.schemas.login_request import LoginRequest
from user_admission.apis.v1.schemas.login_request import login_request
from user_admission.apis.v1.schemas.login_response import LoginResponse
from django.contrib import messages

account = Router(tags=["MemberManagement"])


# login page render router
@account.get("/", response=LoginResponse, url_name='login')
def get_login_page(request: HttpRequest) -> HttpResponse:
    return render(request, "login.html")


@account.post("/")
def post_login_page(request, log_in: login_request = Form(...)):
    # print('0')
    user = authenticate(request, username=log_in.username, password=log_in.password)
    # print('login_request.username:' + log_in.username)
    # print('login_request.password:' + log_in.password)
    if user is not None:
        # print('1')
        login(request, user=user)
        # print('2')
        return redirect('/')
    else:
        messages.error(request, "ID 혹은 비밀번호 오류입니다.")
        return redirect("/")
