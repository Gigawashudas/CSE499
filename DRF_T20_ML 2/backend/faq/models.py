from django.db import models

# Create your models here.


class FAQ(models.Model):
    question = models.CharField(max_length=500, blank=True, null=True)
    answer = models.TextField(max_length=2000, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.question
