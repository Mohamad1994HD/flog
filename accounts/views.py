from django.shortcuts import render, redirect

from .forms import UserLoginForm
# Create your views here.
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    )


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, "user_sign_form.html", {"form": form,
                                "title":"login"}) 

def logout_view(request):
    logout(request)
    return redirect('/')
