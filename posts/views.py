from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.timezone import localtime, now 
from django.db.models import Q
from django.conf import settings

from .models import Post, create_slug
from .forms import PostForm
from .utils import slice_ as sl


def is_search(request=None):
    return request.GET.get('q') 

def get_search_result(qs=None, search_query=None):
    qs = qs.filter(
        Q(title__icontains=search_query)|
        Q(content__icontains=search_query)|
        Q(tags__icontains=search_query)
    ).distinct()
    context = {
        "object_list":qs,
#        "page_title": "Search for a recipe",
    }
    return context 

def index(request):
    qobj = Post.objects
    if not (request.user.is_staff or request.user.is_superuser):
        qs = qobj.random_active()
    else:
        qs = qobj.random()


# search query exists     
    search_query = is_search(request)
    if search_query:
        context = get_search_result(qs, search_query)
        return render(request, "post_list_search.html", context) 

    tip_obj_qs = qs.filter(
                        Q(tags__icontains='tip')
                            ).distinct()
    qs = qs.exclude(id__in=[o.id for o in tip_obj_qs])
    context = {
        "main_post":qs.first(),
        "object_list":sl(
            qs, 
            1, 
            settings.INDEX_MAIN_MAX
            ),
        "rand_object_list": sl(
            qs, 
            settings.INDEX_MAIN_MAX+1, 
            settings.INDEX_ARCHIEVE_MAX
            ),
        "tip_object_list": sl(
            tip_obj_qs, 
            0, 
            settings.INDEX_TIP_MAX
            )
    }
    return render(request, "index.html", context)

def post_list(request):
    qobj = Post.objects
    if not (request.user.is_staff or request.user.is_superuser):
        qs = qobj.random_active()
    else:
        qs = qobj.random()

    context = {
        "object_list" : qs
    }
    search_query = is_search(request)
    if search_query:
        context = get_search_result(qs, search_query)

    return render(request, "post_list_search.html", context) 

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    context = {
        "instance": instance,
        "is_draft": instance.draft,
    }
    return render(request, "post_detail.html", context)

def post_create(request):
    if not (request.user.is_staff or request.user.is_superuser):
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
    if not (request.user.is_staff or request.user.is_superuser):
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
    if not (request.user.is_staff or request.user.is_superuser):
        return HttpResponseRedirect(reverse("posts:index"))

   

    instance = get_object_or_404(Post, slug=slug)
    
    if request.method == 'POST':
        instance.delete()
        return HttpResponseRedirect(reverse("posts:list"))

    context = {
        "instance":instance
    }
    
    return render(request, "post_delete.html", context)


