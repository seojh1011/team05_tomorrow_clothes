from django.test import TestCase

from content_post.services.create_feed_service import create_feed
from user_admission.models import User


class TestCreateService(TestCase):

    def test_create_feed(self):
        # given
        print("dd")
        User.objects.create_user(username="test", password="1234")
        user = User.objects.get(id=1)
        print("dd")
        comment = "comment_comment"
        feeds_img = "chu.jpeg"

        feed = create_feed(user, comment, feeds_img)

        self.assertEqual(feed.writer.username, user.username)

