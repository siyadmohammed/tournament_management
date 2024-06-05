from itertools import combinations

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','password']

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

class Tournament(models.Model):

    def generate_fixtures(self):
        teams = self.teams.all()
        matches = []
        for team1, team2 in combinations(teams, 2):
            # Create a match between each pair of teams
            match = Match.objects.create(tournament=self, team1=team1, team2=team2)
            matches.append(match)
        return matches
class Fixture(models.Model):
    teams = models.ManyToManyField(Team)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tournament.name} - {self.date} - {self.time}"


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team1 = models.ForeignKey('Team', related_name='team1_matches', on_delete=models.CASCADE)
    team2 = models.ForeignKey('Team', related_name='team2_matches', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Scheduled')

    # Additional fields and methods as needed

    def __str__(self):
        return f"{self.team1} vs {self.team2} ({self.tournament})"