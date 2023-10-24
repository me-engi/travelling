# bookings/admin.py
from django.contrib import admin
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'tour', 'traveler_name', 'phone_number', 'email', 'id_proof_type', 'payment_status')
    search_fields = ('traveler_name', 'email', 'tour__name')
    list_filter = ('id_proof_type', 'payment_status')

    actions = ['view_booking']

    def view_booking(self, request, queryset):
        # Redirect to the change view of the first selected object
        if queryset.count() == 1:
            obj = queryset.first()
            change_url = reverse('admin:%s_%s_change' % (obj._meta.app_label,  obj._meta.model_name),  args=[obj.id])
            return HttpResponseRedirect(change_url)

    view_booking.short_description = 'View selected booking(s)'

admin.site.register(Booking, BookingAdmin)
