from django.core.paginator import Paginator, Page
from django.db.models import QuerySet

from content_post.models import Feeds
from user_admission.models import User


def create_feed(user, feeds_comment, feeds_img):
    user = User.objects.get(username=user)
    return Feeds.objects.create(writer=user, feeds_comment=feeds_comment, feeds_img_url=feeds_img)


def get_feed_list(page: int, limit: int) -> Page:
    return Paginator(Feeds.objects.order_by("-id"), limit).page(page)
