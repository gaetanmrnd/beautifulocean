from django.db import models
from django.utils import timezone


class Credit(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title