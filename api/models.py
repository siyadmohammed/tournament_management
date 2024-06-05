from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.TextField()
    contact_email = models.EmailField()
    registered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    teams = models.ManyToManyField(Team)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tournament.name} - {self.date} - {self.time}"
