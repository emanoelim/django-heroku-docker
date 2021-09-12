from django.db import models


class AppModel(models.Model):
    nome = models.CharField(max_length=100)
