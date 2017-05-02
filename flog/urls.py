from django.conf.urls import url, include, handler500, handler404
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from .views import about_view, err_404_handler, err_500_handler
from accounts.views import (login_view, logout_view)


# ERROR handlers
handler500 = err_500_handler
handler404 = err_404_handler 

# URL patterns
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_view, name='login'),
    url(r'^logout/', logout_view, name='logout'), 
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^about/$', about_view, name='about'),
    url(r'^', include('posts.urls', namespace='posts')), 
    
]

# only during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

