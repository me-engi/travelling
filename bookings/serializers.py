# bookings/serializers.py
from rest_framework import serializers
from .models import Booking

class BookingDetailSerializer(serializers.ModelSerializer):
    id_proof_upload = serializers.SerializerMethodField()
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = '__all__'

    def get_id_proof_upload(self, instance):
        return instance.id_proof_upload.url if instance.id_proof_upload else None

    def get_photo(self, instance):
        return instance.photo.url if instance.photo else None

class BookingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    # You can add any custom validation or field behavior specific to creating bookings here
