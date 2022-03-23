import json

from django.http import HttpRequest
from ninja import Router

content = Router(tags=["Content_CRUD"])


@content.post("", url_name="weather")
def get_weather(request: HttpRequest)-> json:
    return {'data':'test'}
