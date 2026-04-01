from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        un = request.POST.get("username")
        em = request.POST.get("email")
        password = request.POST.get("password")
        obj = User.objects.filter(username=un).exists()

        if obj:
            return render(request, "register.html", {"error": "User Already Exists..Try New User Name"})

        obj = User.objects.create_user(username=un, password=password, email=em)
        obj.save()
        return redirect("login")

    return render(request, "register.html")


def login(request):
    if request.method == "POST":
        un = request.POST.get("username")
        ps = request.POST.get("password")

        try:
            User.objects.get(username=un)
        except User.DoesNotExist:
            return render(request, "login.html", {"error": "User Does Not Exist"})

        user = authenticate(request, username=un, password=ps)

        if user is not None:
            auth_login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid password"})

    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect("login")
