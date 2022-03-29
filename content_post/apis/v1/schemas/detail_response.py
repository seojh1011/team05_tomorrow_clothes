from datetime import date

from ninja import Schema
from ninja.orm import create_schema

from user_admission.models import User


class DetailResponse(Schema):
    HttpResponse: str

    id: int
    feeds_comment: str
    created_at: date
    writer_id: int
    feeds_img_url: str
    comment_writer: int
    comment: str


class CommentResponse(Schema):
    id: int
    comment_writer: int
    comment: str

FeedSchema = create_schema(User)
