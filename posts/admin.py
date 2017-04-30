from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Post
# Register your models here.
class PostCreateForm(SummernoteModelAdmin):
    pass

admin.site.register(Post, PostCreateForm)
