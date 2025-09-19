from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from login_app.forms import MyUserCreationForm

# Create your views here.


def login_app(request):
    if request.user.is_authenticated:
        return redirect("/")

    else:

        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("pass")
            user = authenticate(request, username=username, password=password)
            if user is None:
                error = 'username or password is wrong'
                return render(request, 'login.html', context={'error': error})
            else:
                login(request, user)
                return redirect('/')
    return render(request, "login.html")

def logout_app(request):
    logout(request)
    return redirect("/")



def user_signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    return render(request, "signin.html", context={'form': form})
