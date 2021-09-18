from django.db import models


class User(models.Model):
    name = models.CharField(max_length=15)
    age = models.PositiveSmallIntegerField()
    happy = models.BooleanField()
    healthy = models.BooleanField()
    busy = models.BooleanField()

    def __str__(self):
        return self.name