from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


from .views import (
    account_login,
    account_logout,
    account_register,
    account_detail,
    account_edit,
)

urlpatterns = [
# sign
    url(r'^login/', account_login, name='login'),
    url(r'^logout/', account_logout, name='logout'),
    url(r'^signup/', account_register, name='signup'),
# social
    url(r'^social/', include('social_django.urls', namespace='social')),  
# account    
    url(r'^(?P<username>.+)/edit/$', account_edit, name='edit'),
    url(r'^(?P<username>.+)/$', account_detail, name='detail'),

# password_reset
    url(
        r'^password/forgot/$', auth_views.password_reset, 
        {
            'template_name':'accounts/registration/password_reset_form.html',
            'email_template_name': 'accounts/registration/password_reset_email.html',
            'subject_template_name': 'accounts/registration/password_reset_subject.txt',    
            'post_reset_redirect': 'accounts:password_reset_done',
        },
        name='password_reset'
    ),
    url(r'^password/forgot/done/$', 
        auth_views.password_reset_done, 
        {'template_name':'accounts/registration/password_reset_done.html'},
        name='password_reset_done'
    ),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, 
        {
            'template_name':'accounts/registration/password_reset_confirm.html',
            'post_reset_redirect': 'accounts:password_reset_complete',

        },
        name='password_reset_confirm'
    ),
    url(r'^password/reset/done/$', 
        auth_views.password_reset_complete, 
        {'template_name':'accounts/registration/password_reset_complete.html'},
        name='password_reset_complete'
    ), 
]
