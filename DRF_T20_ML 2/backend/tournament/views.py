from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from account.models import UserAccount

# Create your views here.


class HomeListView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userpanel/index.html')

    def post(self, request, *args, **kwargs):
        pass


class DownloadView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userpanel/download.html')

    def post(self, request, *args, **kwargs):
        pass
