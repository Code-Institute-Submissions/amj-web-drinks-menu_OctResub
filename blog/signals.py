from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.contrib import messages

from django.contrib.auth.models import User
from .models import Post


@ receiver(post_delete, sender=Post)
def deleteBlog(sender, instance, **kwargs):
    pass
# @receiver(post_save, sender=User)
# def createProfile(sender,instance,created,**kwargs):
#     if created:
#         user = instance
#         profile = Profile.objects.create