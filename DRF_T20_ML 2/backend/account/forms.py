from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms


from account.models import Profile, UserAccount
User = get_user_model()


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'email_id', 'date_joined']


class RegistrationForm(UserCreationForm):
    # first_name = forms.CharField(label='First Name', min_length=3, max_length=150)
    # last_name = forms.CharField(label='Last Name', min_length=3, max_length=150)
    # email = forms.EmailField(label='Email')
    # password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    #
    # def first_name_clean(self):
    #     first_name = self.cleaned_data['first_name']
    #     if first_name is None:
    #         raise ValidationError("Please fill out this field")
    #     return first_name
    #
    # def last_name_clean(self):
    #     last_name = self.cleaned_data['first_name']
    #     if last_name is None:
    #         raise ValidationError("Please fill out this field")
    #     return last_name
    #
    # def email_clean(self):
    #     email = self.cleaned_data['email'].lower()
    #     new = User.objects.filter(email=email)
    #     if new.count():
    #         raise ValidationError(" Email already exist")
    #     return email
    #
    # def clean_password2(self):
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']
    #
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Password doesn't match")
    #     return password2
    #
    # def save(self, commit=True):
    #     user = User.objects.create_user(
    #         self.cleaned_data['first_name'],
    #         self.cleaned_data['last_name'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password1']
    #     )
    #     return user

    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
