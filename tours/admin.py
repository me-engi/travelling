# tours/admin.py
from django.contrib import admin
from .models import Tour, TourAvailability

class TourAvailabilityInline(admin.TabularInline):
    model = TourAvailability
    extra = 1

class TourAdmin(admin.ModelAdmin):
    inlines = [TourAvailabilityInline]

admin.site.register(Tour, TourAdmin)
