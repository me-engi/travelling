# bookings/views.py
from rest_framework import generics
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingDetailSerializer

class BookingListView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer

class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingDetailSerializer
