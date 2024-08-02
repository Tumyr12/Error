from django.db import models

# Create your models here.
class Video(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=55)
    embed = models.TextField(unique=True)
    