from typing import Any, Optional, Dict

from django.core.paginator import Page, Paginator
from django.db.models import QuerySet
from ninja import UploadedFile

from content_post.models.contents import Feeds
from user_admission.models import User


# feed를 인위적으로 만들어 내는 함수
def create_feed(username: str, feeds_comment: str, feeds_img: UploadedFile) -> Feeds:
    user: User = User.objects.get(username=username)
    feeds: Feeds = Feeds.objects.create(
        writer=user,
        feeds_comment=feeds_comment,
        feeds_img_url=feeds_img
    )
    print(type(feeds))
    return feeds


# feed_list를 가져오는 서비스
def get_feed_list(page: int, limit: int) -> Optional[Page]:
    page_list = Paginator(Feeds.objects.order_by("-id"), limit)
    print("count :", page_list.num_pages)
    print(type(int(page)))
    if int(page) > page_list.num_pages:
        return None
    pages = page_list.page(page)
    print("pages : ", pages)
    return pages
