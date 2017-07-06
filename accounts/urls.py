from django.conf.urls import url

from .views import (
    account_login,
    account_logout,
    account_register,
    account_detail,
    account_edit,
)

urlpatterns = [
    url(r'^login/', account_login, name='login'),
    url(r'^logout/', account_logout, name='logout'),
    url(r'^signup/', account_register, name='signup'),

    url(r'^(?P<username>\w+)/edit/$', account_edit, name='edit'),
    url(r'^(?P<username>\w+)/$', account_detail, name='detail'),
]
