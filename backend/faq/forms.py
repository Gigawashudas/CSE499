from dataclasses import field
from django.forms.models import ModelForm
from faq.models import (
    FAQ
)


class FAQForm(ModelForm):
    class Meta:
        model = FAQ
        fields = '__all__'
