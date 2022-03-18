from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ninja import Router, Form, File, UploadedFile

from content_post.apis.v1.schemas.detail_response import DetailResponse
from content_post.models import Feeds
from user_admission.models import User

content = Router(tags=["Content_CRUD"])


# detail page render router
@content.get("", response=DetailResponse)
def get_detail_page(request: HttpRequest) -> HttpResponse:
    return render(request, "detail.html")


# detail/feeds
@content.get("/feeds/", response=DetailResponse)
def get_feeds_page(request: HttpRequest) -> HttpResponse:
    return render(request, "add.html")


# detail/feeds/ (추가)
@content.post('/feeds/', response=DetailResponse)
@login_required(login_url='/login/')
def post_feeds_page(request, writer_id: int = 9, feeds_comment: str = Form(...), feeds_img_url: UploadedFile = File(...)):
    writer = get_object_or_404(User, id=writer_id)
    Feeds.objects.create(feeds_comment=feeds_comment, feeds_img_url=feeds_img_url, writer=writer)
    feed_id = Feeds.objects.order_by('-id')[0].id
    return redirect("/detail/feeds/" + str(feed_id) + "/")


# detail/feeds/<int:feed_id> 수정
@content.put('/feeds/{feed_id}/', response=DetailResponse)
def put_feeds_page(request, feed_id: int, feeds_comment: str = Form(...), feeds_img_url: UploadedFile = File(...)):
    new_feed = Feeds.objects.get_object_or_404(Feeds, id=feed_id)
    new_feed.feeds_comment = feeds_comment
    new_feed.feeds_img_url = feeds_img_url
    new_feed.save()
    return redirect("/detail/feeds/" + str(feed_id) + "/")


# detail/feeds/<int:feed_id> 삭제
@content.delete('/feeds/{feed_id}', response=DetailResponse)
def delete_feeds_page(request, feed_id):
    delete_feed = get_object_or_404(Feeds, id=feed_id)
    delete_feed.delete()
    return redirect('/')