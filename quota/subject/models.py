from django.db import models

# Create your models here.


class Subject(models.Model):
    Subject_id = models.CharField(max_length=8)
    name = models.CharField(max_length=64)
    quantity = models.IntegerField()
    semester = models.IntegerField(default=None)
    year = models.IntegerField(default=None)
    state = models.BooleanField(default=True)
    
    


