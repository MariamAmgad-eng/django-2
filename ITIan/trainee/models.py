from django.db import models

# Create your models here.
from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='trainee_pics/', null=True, blank=True)
    phone = models.CharField(max_length=15)
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    def __str__(self):
        return self.name
