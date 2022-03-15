from django.db import models

from user_admission.models import User


class Feeds(models.Model):
    class Meta:
        db_table = "FEED"

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    feeds_comment = models.TextField()
    feeds_img_url = models.FileField(upload_to="images", blank=True, null=True)
    writer = models.ForeignKey(User,related_name="user_feed", on_delete=models.CASCADE)
    style_tag = models.CharField(max_length=100, null=True)
    scrape = models.ManyToManyField(User)
    scrapes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta:
        db_table = "COMMENT"

    feed_id = models.ForeignKey(Feeds, related_name="feed_comment", db_column="feed_id" ,on_delete=models.CASCADE)
    comment = models.TextField()
    step = models.IntegerField(default=0)
    comment_num = models.ForeignKey("self", on_delete=models.CASCADE , null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

