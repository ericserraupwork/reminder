from smtplib import SMTPException

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.template.loader import get_template
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta

from patient.models import Appointment


def reminder_email():
    print("reminder_email start")
    start_date = timezone.now()
    end_date = start_date + timedelta(seconds=60 * 60 * 24)
    template_name = "reminder-email.html"
    appointments = Appointment.objects.filter(time__range=[start_date, end_date], is_sent=False).all()

    print("reminder_email")
    print(start_date, end_date)
    print(len(appointments))
    print("***************")
    for appointment in appointments:
        appointment.is_sent = True
        appointment.save()
        code = {
            'name': appointment.name,
            'time': appointment.time,
        }
        html_message = get_template(template_name).render(code)
        combine_name = 'Reminder' + ' <' + settings.EMAIL_HOST_USER + '>'
        try:
            send_mail(
                subject='Reminder',
                message='Reminder message',
                html_message=html_message,
                from_email=combine_name,
                recipient_list=[appointment.email],
                fail_silently=False,
            )
        except SMTPException:  # pragma: no cover
            print({
                'message': _('Email message has not been sent.')
            })

