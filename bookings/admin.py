from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'time', 'created_at')
    list_filter = ('date', 'user')
    search_fields = ('title', 'description', 'user__username')
    ordering = ('-created_at',)