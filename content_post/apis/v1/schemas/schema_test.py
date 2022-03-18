from ninja.orm import create_schema

from user_admission.models import User

UserSchema = create_schema(User, exclude=["username", "password", "email"])
