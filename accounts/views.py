from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404,
    HttpResponseRedirect,
    )

from django.contrib.auth.models import Group, User

from .forms import (
    UserLoginForm, 
    UserRegisterForm,
    ProfileForm,
    )

# Create your views here.
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    )

#from .models import Editors

def account_register(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
       
        new_user = authenticate(username=user.username, password=password)

        login(request, new_user)
        return redirect('/')

    context = {
        "form": form,
        "title": "Register",
    }
    return render(request, "user_sign_form.html", context)

def account_login(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    return render(request, "user_sign_form.html", {"form": form,
                                "title":"login"}) 

def account_logout(request):
    logout(request)
    return redirect('/')


def account_detail(request, pk=None):
    user = get_object_or_404(User, id=pk)
    context = {
        'user': user,
        'profile': user.profile,
        'posts': user.post_set.active(),
    }
    return render(request, 'account_detail.html', context)

def account_edit(request, pk=None):
    user = get_object_or_404(User, id=pk)
    if not (request.user == user):
        if not request.user.is_superuser:
            return HttpResponseRedirect(user.profile.get_absolute_url())

    form = ProfileForm(request.POST or None, request.FILES or None, instance=user.profile)
    if form.is_valid():
        instance = form.save(commit=True) 
        return HttpResponseRedirect(instance.get_absolute_url()) 

    context = {
        "form":form, 
        "title": 'Edit profile',
    }

    return render(request, "post_form.html", context)
