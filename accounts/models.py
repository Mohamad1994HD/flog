from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType 
from django.contrib.auth.models import Group, Permission, User
from django.core.urlresolvers import reverse
# Create your models here.



def upload_location(instance, filename):
    return "profiles/%s/%s" %(instance, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=upload_location,
        null=True,
        blank=True
    )      
    bio = models.CharField(max_length=240, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)
    def __unicode__(self):
        return str(self.user.username) 
    
    def get_absolute_url(self):
        return reverse("accounts:detail", kwargs={"pk":self.user.pk})

def create_user_profile(sender, instance, created, **kwargs):
    # check if first creation, assign a new profile
    if created:
        Profile.objects.create(user=instance)

models.signals.post_save.connect(create_user_profile, sender=User)
