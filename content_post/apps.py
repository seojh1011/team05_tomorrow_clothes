from django.apps import AppConfig
import pandas as pd
from pandas import DataFrame


class ContentPostConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "content_post"
    url = "add.xlsx"
    exel = pd.read_excel(url, engine='openpyxl')

    @staticmethod
    def get_exel(self) -> DataFrame:
        url = "add.xlsx"
        return pd.read_excel(url, engine='openpyxl')