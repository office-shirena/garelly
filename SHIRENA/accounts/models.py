from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    companycode = models.CharField(max_length=5, blank=True)
    #companyname = models.CharField(max_length=20, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
    
    
