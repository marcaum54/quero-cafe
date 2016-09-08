from django.db import models
from django.contrib.auth.models import User


class User(User):

    slack_nickname = models.CharField(max_length=128)
    flag_date = models.DateTimeField(null=True)
    voluntary_date = models.DateTimeField(null=True)
    justification = models.TextField(null=True)