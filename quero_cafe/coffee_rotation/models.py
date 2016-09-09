from django.db import models
from django.contrib.auth.models import User

class Cycle(models.Model):
    name = models.CharField(max_length=128, null=False)

class Turn(models.Model):
    cycle = models.ForeignKey(Cycle, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    made_date = models.DateTimeField(null=True)
    voluntary_date = models.DateTimeField(null=True)

    justification = models.TextField(null=True)

    deleted_at = models.DateTimeField(null=True)