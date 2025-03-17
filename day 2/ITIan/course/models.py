# Create your models here.
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    course_image = models.ImageField(upload_to='course_pics/', null=True, blank=True)

    def __str__(self):
        return self.title

