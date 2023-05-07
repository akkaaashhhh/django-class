from django.db import models

class Blog(models.Model):
    title=models.CharField(max_length=20)
    description = models.TextField()
    text=models.TextField()
# Create your models here.
