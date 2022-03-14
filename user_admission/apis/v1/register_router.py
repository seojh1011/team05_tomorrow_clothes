from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from ninja import Router

from user_admission.apis.v1.schemas.register_response import RegisterResponse

register = Router(tags=["MemberManagement"])


# register page render router
@register.get("/", response=RegisterResponse)
def get_register_page(request: HttpRequest) -> HttpResponse:
    return render(request, "register.html")
