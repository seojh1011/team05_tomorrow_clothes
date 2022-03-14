from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from ninja import Router

from content_post.apis.v1.schemas.main_response import MainResponse

main = Router()


@main.get("", response=MainResponse)
def get_main_page(request: HttpRequest) -> HttpResponse:
    return render(request, "main.html")
