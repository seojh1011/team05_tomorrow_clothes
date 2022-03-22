from typing import Any, Union

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from ninja import Router

from content_post.apis.v1.schemas.main_response import MainResponse
from content_post.services.get_feed_list_service import get_feed_list

content = Router(tags=["Content_CRUD"])


# main page render router
@content.get("", url_name="main", response=list[MainResponse])
def get_main_page(request: HttpRequest) -> HttpResponse:
    page: int = 1
    limit: int = 10
    # print(request.GET)
    if len(request.GET) > 0:

        page = request.GET["page"]  # type: ignore
        limit = request.GET["limit"]  # type: ignore
        # print("page:", page)
        # print("limit :", limit)
        pages = get_feed_list(page, limit)

        if pages is None:
            return list()
        # print(pages[0].feeds_img_url)
        # print(list(pages))
        return list(pages)

    # print(limit)
    pages = get_feed_list(page, limit)
    return render(request, "main.html", {"test": pages})
