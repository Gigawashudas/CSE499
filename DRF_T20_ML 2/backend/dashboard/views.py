import imp
import os
from django.shortcuts import redirect, render

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import DeleteView

from django.contrib import messages

from account.models import Profile
from tournament.models import Tournament, TeamName, VenueName
from faq.models import FAQ


from tournament.forms import (
    TournamentForm,
    TeamNameForm,
    VenueNameForm
)
from faq.forms import (
    FAQForm
)

# dashboard index


class DashboardIndexView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return render(request, 'dashboard/index.html')
            else:
                return redirect('tournament:index')
        else:
            return redirect('account:login')

    def post(self, request, *args, **kwargs):
        pass


# user view
class UserListView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            users = Profile.objects.all().order_by('-id')
            context = {
                'users': users
            }
            return render(request, 'dashboard/user_list.html', context)
        else:
            return redirect('tournament:index')

    def post(self, request, *args, **kwargs):
        pass


# Tournament View
class TournamentListView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'superuser':
                tournaments = Tournament.objects.all().order_by('-id')
                context = {
                    'tournaments': tournaments
                }
                return render(request, 'dashboard/tournament_list.html', context)
            else:
                return redirect('tournament:index')
        else:
            return redirect('tournament:index')

    def post(self, request, *args, **kwargs):
        pass


class AddNewTournament(TemplateView):
    def get(self, request, *args):
        if request.user.user_type == 'superuser':
            form = TournamentForm()
            context = {
                'form': form
            }
            return render(request, 'dashboard/add_form.html', context)
        else:
            return redirect('tournament:index')

    def post(self, request, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                form = TournamentForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Tournament added successfully!")
                    return redirect('dashboard:tournaments')

            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:tournament_list')
        else:
            return redirect('tournament:index')


class TournamentUpdateView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        tournament = Tournament.objects.get(id=pk)
        form = TournamentForm(instance=tournament)
        context = {
            'form': form
        }
        return render(request, 'dashboard/add_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                tournament = Tournament.objects.get(id=pk)
                form = TournamentForm(request.POST, instance=tournament)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Tournament updated successfully!")
                    return redirect('dashboard:tournaments')
            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:tournaments')
        else:
            return redirect('tournament:index')


class TournamentDeleteView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            tournament = Tournament.objects.get(id=pk)
            tournament.delete()
            messages.success(request, "Tournament deleted successfully!")
            return redirect('dashboard:tournaments')
        else:
            return redirect('tournament:index')


# Team name view
class TeamListView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'superuser':
                teams = TeamName.objects.all().order_by('-id')
                context = {
                    'teams': teams
                }
                return render(request, 'dashboard/team_list.html', context)
            else:
                return redirect('tournament:index')
        else:
            return redirect('tournament:index')

    def post(self, request, *args, **kwargs):
        pass


class AddNewTeamName(TemplateView):
    def get(self, request, *args):
        if request.user.user_type == 'superuser':
            form = TeamNameForm()
            context = {
                'form': form
            }
            return render(request, 'dashboard/add_form.html', context)
        else:
            return redirect('tournament:index')

    def post(self, request, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                form = TeamNameForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Team name added successfully!")
                    return redirect('dashboard:teams')

            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:teams')
        else:
            return redirect('tournament:index')


class TeamNameUpdateView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        team = TeamName.objects.get(id=pk)
        form = TeamNameForm(instance=team)
        context = {
            'form': form
        }
        return render(request, 'dashboard/add_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                team = TeamName.objects.get(id=pk)
                form = TeamNameForm(request.POST, instance=team)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Team name updated successfully!")
                    return redirect('dashboard:teams')
            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:teams')
        else:
            return redirect('tournament:index')


class TeamNameDeleteView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            team = TeamName.objects.get(id=pk)
            team.delete()
            messages.success(request, "Team name deleted successfully!")
            return redirect('dashboard:teams')
        else:
            return redirect('tournament:index')


# Team venue view

class VenueListView(TemplateView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.user_type == 'superuser':
                venues = VenueName.objects.all().order_by('-id')
                context = {
                    'venues': venues
                }
                return render(request, 'dashboard/venue_list.html', context)
            else:
                return redirect('tournament:index')
        else:
            return redirect('tournament:index')

    def post(self, request, *args, **kwargs):
        pass


class AddNewVenue(TemplateView):
    def get(self, request, *args):
        if request.user.user_type == 'superuser':
            form = VenueNameForm()
            context = {
                'form': form
            }
            return render(request, 'dashboard/add_form.html', context)
        else:
            return redirect('tournament:index')

    def post(self, request, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                form = VenueNameForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Venue name added successfully!")
                    return redirect('dashboard:venues')

            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:venues')
        else:
            return redirect('tournament:index')


class VenueNameUpdateView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        venue = VenueName.objects.get(id=pk)
        form = VenueNameForm(instance=venue)
        context = {
            'form': form
        }
        return render(request, 'dashboard/add_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                venue = VenueName.objects.get(id=pk)
                form = VenueNameForm(request.POST, instance=venue)
                if form.is_valid():
                    form.save()
                    messages.success(request, "Venue name updated successfully!")
                    return redirect('dashboard:venues')
            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:venues')
        else:
            return redirect('tournament:index')


class VenueNameDeleteView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            venue = VenueName.objects.get(id=pk)
            venue.delete()
            messages.success(request, "Venue name deleted successfully!")
            return redirect('dashboard:venues')
        else:
            return redirect('tournament:index')


# faq view
class FAQListView(ListView):
    def get(self, request, *args, **kwargs):
        if request.user.user_type == 'superuser':
            faqs = FAQ.objects.all().order_by('-id')
            context = {
                'faqs': faqs
            }
            return render(request, 'dashboard/faq_list.html', context)
        else:
            return redirect('store:index')

    def post(self, request, *args, **kwargs):
        pass


class AddNewFAQ(TemplateView):
    def get(self, request, *args):
        if request.user.user_type == 'superuser':
            form = FAQForm()
            context = {
                'form': form
            }
            return render(request, 'dashboard/add_form.html', context)
        else:
            return redirect('dashboard:index')

    def post(self, request, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                form = FAQForm(request.POST, request.FILES)
                if form.is_valid():
                    form.save()
                    messages.success(request, "FAQ added successfully!")
                    return redirect('dashboard:faq_list')
            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:faq_list')
        else:
            return redirect('store:index')


class FAQUpdateView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        faq = FAQ.objects.get(id=pk)
        form = FAQForm(instance=faq)
        context = {
            'form': form
        }
        return render(request, 'dashboard/add_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            if request.method == 'post' or request.method == 'POST':
                faq = FAQ.objects.get(id=pk)
                form = FAQForm(request.POST, request.FILES, instance=faq)
                if form.is_valid():
                    form.save()
                    messages.success(request, "FAQ updated successfully!")
                    return redirect('dashboard:faq_list')
            else:
                messages.success(request, "Something wrong!")
                return redirect('dashboard:faq_list')
        else:
            return redirect('tournament:index')


class FAQDeleteView(TemplateView):
    def get(self, request, pk, *args, **kwargs):
        if request.user.user_type == 'superuser':
            faq = FAQ.objects.get(id=pk)
            faq.delete()
            messages.success(request, "FAQ deleted successfully!")
            return redirect('dashboard:faq_list')
        else:
            return redirect('tournament:index')
