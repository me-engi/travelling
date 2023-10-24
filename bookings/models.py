# bookings/models.py
from django.db import models
from tours.models import Tour

class Booking(models.Model):
    ID_PROOF_CHOICES = [
        ('aadhar_card', 'Aadhar Card'),
        ('citizenship', 'Citizenship'),
        ('passport', 'Passport'),
    ]

    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    traveler_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    id_proof_type = models.CharField(max_length=50, choices=ID_PROOF_CHOICES)
    id_proof_upload = models.FileField(upload_to='id_proof_uploads/', default='default/id_proof.pdf') 
    photo = models.ImageField(upload_to='booking_photos/')
    payment_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.traveler_name}'s booking for {self.tour.name}"
