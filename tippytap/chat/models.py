from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):

    created = models.DateTimeField("created", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.SET_NULL, null=True)
    text = models.CharField("text", max_length=255)
