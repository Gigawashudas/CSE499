from django.urls import path
from contactus import views

app_name = 'contactus'
urlpatterns = [
    path('', views.ContactUsView.as_view(), name='contactus_form'),
]
