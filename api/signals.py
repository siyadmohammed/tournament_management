from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Tournament, Team

@receiver(post_save, sender=Tournament)
def send_tournament_notification(sender, instance, created, **kwargs):
    if created:
        teams = Team.objects.all()
        for team in teams:
            send_mail(
                'New Tournament Created',
                f'Dear {team.name}, a new tournament named {instance.name} has been created.',
                'from@example.com',
                [team.contact_email],
                fail_silently=False,
            )
