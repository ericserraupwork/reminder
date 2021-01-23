from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from rest_framework.routers import DefaultRouter

from patient import views

app_name = 'events'
router = DefaultRouter()
router.register('', views.AppointmentView, basename='appointment')

urlpatterns = [
    path('api', include(router.urls)),
    path(_(''), views.PatientView.as_view(), name="patient"),
]
