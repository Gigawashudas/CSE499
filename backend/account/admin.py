from django.contrib import admin
from account.models import Profile, UserAccount

admin.site.register(UserAccount)
admin.site.register(Profile)
