from django.contrib.auth.models import AbstractUser
from django.db import models


def avatar_path(instance, filename):
    print(f'{instance.id}/{filename}')
    return f'{instance.id}/{filename}'


class User(AbstractUser):
    avatar = models.FileField(upload_to=avatar_path, blank=True, null=True)


# class Avatar(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     avatar = models.FileField(upload_to=avatar_path, blank=True, null=True)


class Contact(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email_from = models.EmailField()
    title = models.CharField(max_length=128)
    message = models.TextField()
