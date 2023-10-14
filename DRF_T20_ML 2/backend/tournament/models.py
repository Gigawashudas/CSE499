from django.db import models

# Create your models here.


class Tournament(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    tool_tip = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='images/tournament', default='images/no-image@2x.png', blank=True, null=True)
    score_prediction_model = models.FileField(upload_to='models/score', blank=True, null=True)
    first_innings_win_prediction_model = models.FileField(upload_to='models/first_innings_win', blank=True, null=True)
    second_innings_win_prediction_model = models.FileField(upload_to='models/second_innings_win', blank=True, null=True)
    description = models.TextField(max_length=5000, blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class TeamName(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_team')
    team = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.team)

    class Meta:
        ordering = ['-created']


class VenueName(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_venue')
    city = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.city)

    class Meta:
        ordering = ['-created']
