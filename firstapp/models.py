from django.db import models
from django.urls import reverse
# Create your models here.
class Vehicle(models.Model):
    vehicle_number = models.CharField(max_length = 50)
    vehicle_type = models.CharField(max_length = 120)
    vehicle_model = models.CharField(max_length = 150)
    vehicle_description = models.TextField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
