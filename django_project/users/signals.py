from django.db.models.signals import post_save # this signals gefired after an object is saved!
from django.contrib.auth.models import User # sending the signals
from django.dispatch import receiver
from .models import Profile

# we want to create user profile when an user gets signs up

@receiver(post_save, sender=User)  # here when User will be created it will send the signal post_save which will be recived and if it is created then a profile will also get created
# or say it like this when a user is saved send this 'post_save' signal which will be recived into this function.
def create_proflie(sender, instance, created, **kwargs): # these all paramter are getting passed from the post_save signals 
    if created :
        Profile.objects.create(user = instance)


@receiver(post_save, sender=User)
def save_proflie(sender, instance, **kwargs):
    instance.profile.save()