from ninja import Schema


class MainResponse(Schema):
    HttpResponse: str = None
    feeds_img_url : str = None
