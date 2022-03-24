from django.http import HttpRequest, HttpResponse
from ninja import Router, UploadedFile

from content_post.models import Feeds
from user_admission.models import User

content = Router(tags=["MyPage"])

@content.post("/mypage/")
def get_my_page(request: HttpRequest) -> HttpResponse:
    user_id = '16'
    # user_id = request.user.id
    user_feeds = Feeds.objects.filter(writer_id=user_id)
    scrap_feeds = Feeds.objects.filter(scrape=user_id)
    user_information = User.objects.get(id=user_id)



@content.post("/mypage/update/")
def update_profile(request: HttpRequest,feeds_img_url: UploadedFile,) -> HttpResponse:
    user_id = '16'
    # user = request.user
    user = User.objects.get(id=user_id)
    user.pro_img_url = feeds_img_url
    user.save()




