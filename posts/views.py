from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.timezone import localtime, now 
from django.db.models import Q
from django.conf import settings
from .models import Post, create_slug
from .forms import PostForm
# Create your views here.

def index(request):
    qobj = Post.objects
    if not request.user.is_staff or not request.user.is_superuser:
        qs = qobj.active()
    else:
        qs = qobj.all()
     
    search_query = request.GET.get('q')
    if search_query:
        qs = qs.filter(
            Q(title__icontains=search_query)|
            Q(content__icontains=search_query)|
            Q(tags__icontains=search_query)
        ).distinct()
        context = {
            "object_list":qs,
#            "page_title": "Search for a recipe",
        }
        return render(request, "post_list_search.html", context)
    tip_obj_lst = qs.filter(
                        Q(tags__icontains='tip')
                            ).distinct()
    context = {
        "main_post":qs.first(),
        "object_list":qs[:settings.INDEX_POST_MAX],
        "rand_object_list": Post.objects.random(settings.INDEX_POST_MAX),
        "tip_object_list": tip_obj_lst,
    }
    return render(request, "index.html", context)

def post_list(request):
    qobj = Post.objects
    if not request.user.is_staff or not request.user.is_superuser:
        qs = qobj.active()
    else:
        qs = qobj.all()

    search_query = request.GET.get('q')
    if search_query:
        qs = qs.filter(
            Q(title__icontains=search_query)|
            Q(content__icontains=search_query)|
            Q(tags__icontains=search_query)
        ).distinct()
    context = {
        "object_list": qs,
#        "page_title": "Search for a recipe",
    }

    return render(request, "post_list_search.html", context) 

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "instance": instance,
        "is_draft": instance.draft,
    }
    return render(request, "post_detail.html", context)

def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponseRedirect(reverse("posts:index"))

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False) # modify
        instance.slug = create_slug(instance)
        if not instance.draft:
            instance.publish = localtime(now()).date()
        instance.save() 
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form":form,
        "title": "Create a new yummy post"
    } 
    return render(request, "post_form.html", context) 

def post_edit(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponseRedirect(reverse("posts:index"))

    instance = get_object_or_404(Post, slug=slug) 
    form = PostForm(request.POST or None,request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        if not instance.draft:
            instance.publish = localtime(now()).date()
        instance.save()
 
        return HttpResponseRedirect(instance.get_absolute_url()) 
    context = {
        "form": form,
        "title": instance.title,
    }
    return render(request, "post_form.html", context)

def post_delete(request, slug=None):
    if not request.user.is_staff or not request.user.is_superuser:
        return HttpResponseRedirect(reverse("posts:index"))

   

    instance = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect(reverse("posts:list"))

    context = {
        "instance":instance
    }
    
    return render(request, "post_delete.html", context)


