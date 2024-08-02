from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=55)
    text = models.TextField()
    imagel = models.ImageField(upload_to='blog/img/')
    likes = models.PositiveIntegerField(default=0)
    draft = models.BooleanField(default=False)
    is_published = models.DateTimeField(auto_now_add=True)

