from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


from contactus.models import Contactus


class ContactForm(ModelForm):
    class Meta:
        model = Contactus
        fields = '__all__'
        exclude = ['is_reply', 'created']

