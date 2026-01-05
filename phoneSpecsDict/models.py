from django.db import models

# Create your models here.
class MainSpec(models.Model):

    name = models.CharField(max_length = 255)   # Name(brand) of the phone
    property = models.CharField(max_length = 255) # Description or characteristic of the phone

    def __str__(self):
        return f"{self.name} - {self.property}"