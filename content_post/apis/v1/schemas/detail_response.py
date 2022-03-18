from datetime import date

from ninja import Schema


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
