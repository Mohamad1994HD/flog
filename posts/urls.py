from django.conf.urls import url

from .views import (
    post_list,
    post_detail,
    post_edit,
    post_create,
    post_delete,
    index,
    )

urlpatterns = [
    url(r'^$', index, name='index'), 
    url(r'^search/$', post_list, name='list'),
    url(r'^posts/create/$', post_create, name='create'),
    url(r'^posts/(?P<slug>[-\w]+)/$', post_detail, name='detail'),
    url(r'^posts/(?P<slug>[-\w]+)/edit/$', post_edit, name='edit'), 
    url(r'^posts/(?P<slug>[-\w]+)/delete/$', post_delete, name='delete'),
    
    url(r'^posts/(?P<slug>[-\w]+)/translation/(?P<lang>\w+)/$', post_delete, name='translation'),
    
]
