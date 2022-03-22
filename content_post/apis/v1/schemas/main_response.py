from ninja import Schema


class MainResponse(Schema):
    HttpResponse: str = ""
    feeds_img_url: str = ""
