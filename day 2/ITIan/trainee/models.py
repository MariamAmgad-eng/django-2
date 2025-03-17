from django.db import models

# Create your models here.
from django.db import models

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to='trainee_pics/', null=True, blank=True)

    def __str__(self):
        return self.name
