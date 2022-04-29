from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Song(models.Model):
    title = models.CharField(max_length = 255)
    artist = models.CharField(max_length = 255)
    rating = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.title