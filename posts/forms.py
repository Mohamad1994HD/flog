from django import forms

#from pagedown.widgets import PagedownWidget
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
            'draft',
            'tags',
        ]
