from django.views.generic import TemplateView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from patient.models import Appointment
from patient.serializers import AppointmentSerializer


class PatientView(TemplateView):
    template_name = 'appointment.html'


class AppointmentView(ModelViewSet):
    model = Appointment
    serializer_class = AppointmentSerializer
    permission_classes = (AllowAny,)