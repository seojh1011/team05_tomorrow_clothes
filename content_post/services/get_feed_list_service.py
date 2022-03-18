from django.core.paginator import Paginator, Page
from django.db.models import QuerySet

from content_post.models import Feeds
from user_admission.models import User

# feed를 인위적으로 만들어 내는 함수
def create_feed(user, feeds_comment, feeds_img):
    user = User.objects.get(username=user)
    return Feeds.objects.create(writer=user, feeds_comment=feeds_comment, feeds_img_url=feeds_img)

# feed_list를 가져오는 서비스
def get_feed_list(page: int, limit: int) -> Page:
    page_list = Paginator(Feeds.objects.order_by("-id"), limit)
    print('count :', page_list.num_pages)
    print(type(int(page)))
    if int(page) > page_list.num_pages:
        return None
    pages = page_list.page(page)
    print('pages : ', pages)
    return pages
