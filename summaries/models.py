from django.db import models

# Create your models here.
class DataModel(models.Model):
  source = models.CharField(max_length=400)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
