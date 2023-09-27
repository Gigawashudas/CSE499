from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class TeamName(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_team')
    team = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.team)


class VenueName(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_venue')
    city = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.city)
