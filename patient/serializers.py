from rest_framework import serializers

from patient.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'name', 'email', 'time', 'is_sent')
