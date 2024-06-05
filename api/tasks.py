from celery import shared_task
from django.core.mail import send_mail
from .models import Fixture
import datetime

@shared_task
def send_fixture_notification():
    fixtures = Fixture.objects.filter(date__gte=datetime.date.today())
    for fixture in fixtures:
        for team in fixture.teams.all():
            send_mail(
                'Upcoming Match Notification',
                f'Dear {team.name}, you have a match on {fixture.date} at {fixture.time}.',
                'from@example.com',
                [team.contact_email],
                fail_silently=False,
            )