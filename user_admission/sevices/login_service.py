from user_admission.models import User


def log_in(username: str, password: str) -> None:
    pass


def create_user(username: str, password: str) -> None:
    User.objects.create_user(username=username, password=password)
    # pass


# def create_user(username="root4444", password="1234"):
#     User.objects.create_user(username=username, password=password)
#     return 'true'
