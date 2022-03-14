from django.shortcuts import redirect
from user_admission.models import User

def create_user(request):
    User.objects.create_user(username='root2233', password="1234")
    return redirect("/login/")