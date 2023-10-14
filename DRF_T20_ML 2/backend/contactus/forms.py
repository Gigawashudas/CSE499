from django.forms import ModelForm
from django.contrib.auth.models import User

from django.core.exceptions import ValidationError
from django import forms

from contactus.models import Contactus


from contactus.models import Contactus


class ContactForm(ModelForm):

    # full_name = forms.CharField(label="Full Name", max_length=200,
    #                             required=True, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    # subject = forms.CharField(label="Subject", max_length=200, required=True,
    #                           widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    # email = forms.CharField(label="Email", required=True, max_length=100,
    #                          widget=forms.EmailInput(attrs={'placeholder': 'email@gmail.com'}))
    # message = forms.CharField(required=True, widget=forms.Textarea)
    #
    # def full_name_clean(self):
    #     full_name = self.cleaned_data['full_name']
    #     if full_name is None:
    #         raise ValidationError("Please fill out this field")
    #     return full_name
    #
    # def email_clean(self):
    #     email = self.cleaned_data['email'].lower()
    #     if email is None:
    #         raise ValidationError("Please fill out this field")
    #     return email
    #
    # def subject_clean(self):
    #     subject = self.cleaned_data['subject']
    #     if subject is None:
    #         raise ValidationError("Please fill out this field")
    #     return subject
    #
    # def message_clean(self):
    #     message = self.cleaned_data['message']
    #     if message is None:
    #         raise ValidationError("Please fill out this field")
    #     return message
    #
    # def save(self, commit=True):
    #     contact = Contactus.objects.create(
    #         self.cleaned_data['full_name'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['subject'],
    #         self.cleaned_data['message']
    #     )
    #     return contact

    class Meta:
        model = Contactus
        fields = '__all__'
        exclude = ['is_reply', 'created']

