from django.db import models

# Create your models here.


class Contactus(models.Model):
    full_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(max_length=1000, blank=True, null=True)
    is_reply = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()

    def __str__(self):
        return self.full_name
