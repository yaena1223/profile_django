from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followings = models.ManyToManyField("self", related_name = "followers", symmetrical = False)

# ↓ user생성 시 자동으로 profile이 생성되고 저장될 수 있도록 함 ↓

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

#post_save : user가 생성이 되면 프로필을 만들고 프로필을 저장해라
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
