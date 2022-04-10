from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    longitude = models.CharField(max_length=200)
    latitude = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, 
        on_delete = models.CASCADE,
        default = 1,
    )
