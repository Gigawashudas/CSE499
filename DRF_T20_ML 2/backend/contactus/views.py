import imp
import os
from django.shortcuts import redirect, render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import DeleteView

from django.contrib import messages

# dashboard index


class ContactUsView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userpanel/contactus.html')

    def post(self, request, *args, **kwargs):
        pass
