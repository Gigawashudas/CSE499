from dataclasses import field
from django.forms.models import ModelForm

from tournament.models import (
    Tournament,
    TeamName,
    VenueName
)


class TournamentForm(ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'
        exclude = ['created_at']


class TeamNameForm(ModelForm):
    class Meta:
        model = TeamName
        fields = '__all__'
        exclude = ['created']


class VenueNameForm(ModelForm):
    class Meta:
        model = VenueName
        fields = '__all__'
        exclude = ['created']
