from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from ninja import Router, File
from ninja.files import UploadedFile

from content_post.apis.v1.schemas.main_response import MainResponse
from content_post.services.create_feed_service import create_feed

content = Router(tags=["Content_CRUD"])


# main page render router
@content.post("test/post/", response=MainResponse)
def create_post_page(request: HttpRequest, email: str, comment: str, img: UploadedFile = File(...)):
    a = request.POST
    print(a)
    create_feed(email, comment, img)
    return redirect("/")
