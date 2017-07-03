from django.contrib import admin
from .models import Profile
from .forms import ProfileForm
# Register your models here.
#class AdminProfileForm(admin.ModelAdmin):
#    form = ProfileForm
#
#admin.site.register(Profile, AdminProfileForm)
admin.site.register(Profile)
