from django import template

from contactus.models import Contactus

register = template.Library()


@register.filter
def notifications(user):
    if user.is_authenticated:
        notification = Contactus.objects.filter(is_reply=False).order_by('-id')
        if notification.exists():
            return notification
        else:
            return None
    else:
        return None
