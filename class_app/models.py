from django.db import models

# Create your models here.
class Class(models.Model):
    subject = models.CharField(max_length=255)
