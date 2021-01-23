from django.contrib import admin

from patient.models import Appointment


@admin.register(Appointment)
class SlotAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'time', 'is_sent']
