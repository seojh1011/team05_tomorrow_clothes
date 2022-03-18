from django.test import TestCase

from content_post.models.contents import Feeds
from content_post.services.get_feed_list_service import create_feed
from user_admission.models import User
#
#
# class TestCreateService(TestCase):
#     def test_create_feed(self) -> None:
#         # given
#         print("dd")
#         User.objects.create_user(username="test", password="1234")
#         user: User = User.objects.get(id=1)
#         print("dd")
#         comment = "comment_comment"
#         feeds_img = "chu.jpeg"
#
#         from typing import Optional
#         feed: Feeds = create_feed(user, comment, feeds_img)
#
#         self.assertEqual(feed.writer.username, user.username)
