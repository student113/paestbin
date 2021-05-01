from django.db import models


# Create your models here.

class field(models.Model):
    id = models.TextField(primary_key=True)
    date = models.TextField()
    text = models.TextField()
