from __future__ import unicode_literals

import random

from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db import models
from django.db.models.signals import post_delete
from django.contrib.contenttypes.models import ContentType
from django.utils.safestring import mark_safe
from django.conf import settings

from tagging.models import TaggedItem
from tagging.fields import TagField




def upload_location(instance, filename):
    return "%s/%s" %(instance, filename)

class PostManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostManager, self).filter(draft=False)
    
    def random(self, *args, **kwargs):
        return super(PostManager, self).order_by('?')

    def random_active(self, *args, **kwargs):
        return self.active().order_by('?')

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_location,
                              null=True,
                              blank=True,
                              )
    slug = models.SlugField(unique=True)

    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=True, null=True)

    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True) 
   
    tags = TagField()

    objects = PostManager()
 
    def __unicode__(self):
        return str(self.title)
    
    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug":self.slug})

    
    def is_draft(self):
        return self.draft

    class Meta:
        ordering = ['-publish','-updated']


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def taggeditem_delete(sender,  **kwargs):
    deleted = kwargs['instance']
    try:
        id_ = int(deleted.pk)
    except ValueError:
        return
    ctype = ContentType.objects.get_for_model(deleted)
    item_tags = TaggedItem.objects.filter(
        content_type=ctype,
        object_id=id_,
    )
    item_tags.delete()

post_delete.connect(taggeditem_delete)
