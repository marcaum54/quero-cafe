from django.db import models

class Colaborador(models.Model):
    name = models.CharField(max_length=128)
    slack_nickname = models.CharField(max_length=128)
    flag_date = models.DateTimeField(null=True)