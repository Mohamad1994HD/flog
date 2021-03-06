from django.conf.urls import url, include, handler500, handler404
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from .views import about_view, err_404_handler, err_500_handler

from posts.models import Post

# info dictionary
info_dict = {
    'queryset': Post.objects.active(),
    'date_field': 'updated',
    'title_field': 'title', 
}

# ERROR handlers
handler500 = err_500_handler
handler404 = err_404_handler 

# URL patterns
urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^about/$', about_view, name='about'),
    url(r'^', include('posts.urls', namespace='posts')),
]

# only during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

