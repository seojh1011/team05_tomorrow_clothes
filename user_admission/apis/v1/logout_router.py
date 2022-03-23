from django.contrib.auth import logout as auth_logout
from django.http import HttpRequest
from django.shortcuts import HttpResponse, redirect, render
from ninja import Router

from user_admission.apis.v1.schemas.logout_response import LogoutResponse

account = Router(tags=["MemberManagement"])


@account.get("/", url_name="logout", response=LogoutResponse)
def get_logout(request: HttpRequest) -> HttpResponse:
    auth_logout(request)
    return redirect("/")
