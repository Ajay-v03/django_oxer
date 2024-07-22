from django.db import models

# Create your models here.
class ModelTest(models.Model):
    test_name = models.CharField(max_length=50)
    test_title = models.CharField(max_length=50)
    test_desc = models.TextField()
    
