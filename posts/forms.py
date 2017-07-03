from django import forms

#from pagedown.widgets import PagedownWidget
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget())
    image = forms.ImageField(label='Cover Image', required=False)
    tags = forms.CharField(
                            label='Keywords',
                            widget=forms.TextInput(
                                attrs={'placeholder':'eg. rice, healthy, diet'}
                            )  
                          )
    class Meta:
        model = Post
        fields = [
            'draft',
            'title',
            'image',
            'tags',
            'content',
        ]
