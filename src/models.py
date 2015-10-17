from django.utils.timezone import now
from django.db import models

# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.TextField()
    text = models.TextField()
    created_date =  models.DateTimeField(default=now())


    def __str__(self):
        return self.title

