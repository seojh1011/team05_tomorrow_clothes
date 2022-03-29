from user_admission.models import User


def log_in(username: str, password: str) -> None:
    pass


def create_user(username: str, password: str, email: str, nick_name: str) -> User:
    return User.objects.create_user(
        username=email,
        password=password,
        email=email,
        nick_name=nick_name,
        pro_img_url="images/chu.jpeg",
    )


# def create_user(username="root4444", password="1234"):
#     User.objects.create_user(username=username, password=password)
#     return 'true'
