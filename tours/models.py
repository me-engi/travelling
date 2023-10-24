# tours/models.py
import os
from django.db import models

def tour_image_upload_path(instance, filename):
    # Upload tour images to a directory based on the tour name
    return os.path.join("tour_images", instance.name, filename)

class Tour(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    itinerary = models.TextField()
    days = models.PositiveIntegerField()
    included = models.TextField()
    excluded = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_participants = models.PositiveIntegerField(default=100)
    
    # Add an ImageField for tour images
    image = models.ImageField(upload_to=tour_image_upload_path, blank=True, null=True)

    def __str__(self):
        return self.name

class TourAvailability(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    unavailable_date = models.DateField()

    def __str__(self):
        return f"{self.tour.name} - {self.unavailable_date}"
