import imp
import os
from django.shortcuts import redirect, render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import DeleteView

from django.contrib import messages

from contactus.forms import (
    ContactForm
)

# contactus index


class ContactUsView(TemplateView):
    def get(self, request, *args, **kwargs):
        contact_from = ContactForm()
        context = {
            'form': contact_from
        }
        return render(request, 'userpanel/contactus.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                contact_form = ContactForm()
                context = {
                    'form': contact_form
                }
                messages.success(request, "Message has been sent!")
                return render(request, 'userpanel/contactus.html', context)
            else:
                contact_form = ContactForm()
                context = {
                    'form': contact_form
                }
                return render(request, 'userpanel/contactus.html', context)
