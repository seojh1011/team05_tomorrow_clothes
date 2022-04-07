from datetime import datetime
from typing import Any, Dict, Optional

from django.core.paginator import Page, Paginator
from django.db.models import QuerySet
from ninja import UploadedFile

from content_post.models.contents import Feeds
from user_admission.models import User


# 김윤서
# feed를 인위적으로 만들어 내는 함수
def create_feed(username: str, feeds_comment: str, feeds_img: UploadedFile) -> Feeds:
    user: User = User.objects.get(username=username)
    feeds: Feeds = Feeds.objects.create(
        writer=user, feeds_comment=feeds_comment, feeds_img_url=feeds_img
    )
    return feeds


# 김윤서
# feed_list를 가져오는 서비스
def get_feed_list(page: int, limit: int) -> Optional[Page]:
    # 장고 기능 Pagenator을 사용해서 역순으로 FEEDS객체 가져옴
    page_list = Paginator(Feeds.objects.order_by("-id"), limit)
    # 더이상 페이지가 없다면 None 반환
    if int(page) > page_list.num_pages:
        return None
    pages = page_list.page(page)
    return pages
