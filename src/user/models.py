from django.db import models
from card.models import *

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    companies = models.ManyToManyField('Company')
    def __str__(self):
        return "%s's profile" % self.user

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)
