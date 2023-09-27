import imp
import os
from django.shortcuts import redirect, render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import DeleteView

from django.contrib import messages

from faq.models import FAQ

# Create your views here.

# this is for dashboard index


class FAQView(TemplateView):
    def get(self, request, *args, **kwargs):
        faqs = FAQ.objects.all().order_by('-id')
        context = {
            'faqs': faqs
        }
        return render(request, 'userpanel/faq.html', context)

    def post(self, request, *args, **kwargs):
        pass
