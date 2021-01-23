from django.db import models


class Appointment(models.Model):

    name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=255)
    time = models.DateTimeField(null=True, blank=True)
    is_sent = models.BooleanField(blank=False, default=False)
