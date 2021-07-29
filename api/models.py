from django.db import models

# Create your models here.
class Student(models.Model):
    username=models.CharField(max_length=70)
    data=models.DateField(auto_created=True)
    Note_Text=models.CharField(max_length=500)
    last_updated_date=models.DateTimeField(auto_now_add=True)