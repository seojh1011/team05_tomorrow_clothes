from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from ninja import Router

from content_post.apis.v1.schemas.main_response import MainResponse
from content_post.services.create_feed_service import get_feed_list

content = Router(tags=["Content_CRUD"])


# main page render router
@content.get("", response=MainResponse)
def get_main_page(request: HttpRequest) -> HttpResponse:
    page = get_feed_list(1, 40)
    return render(request, "main.html", {"test": page})
