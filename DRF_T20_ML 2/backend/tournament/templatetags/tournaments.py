from django import template
from tournament.models import Tournament, TeamName, VenueName

register = template.Library()


@register.filter
def tournaments(request):
    if request.user.is_authenticated:
        tournament = Tournament.objects.all().order_by('-id')
        return tournament
    else:
        # tournament = Tournament.objects.all().order_by('-id')
        # return tournament
        return None

