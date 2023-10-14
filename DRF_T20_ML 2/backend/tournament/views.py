from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView

from django.contrib import messages

from account.models import UserAccount

from tournament.models import Tournament, TeamName, VenueName

# Machine Learning

import os
import pickle
import pandas as pd
import numpy as np
import math

import xgboost
from xgboost import XGBRegressor

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder


# Create your views here.


class HomeListView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userpanel/index.html')

    def post(self, request, *args, **kwargs):
        pass


class ScorePredictionView(TemplateView):
    def get(self, request, pk, *args):
        item = Tournament.objects.get(id=pk)
        teams = TeamName.objects.filter(tournament=item)
        venues = VenueName.objects.filter(tournament=item)

        context = {
            'tournament': item,
            'teams': teams,
            'venues': venues
        }

        return render(request, 'userpanel/score_prediction_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.method == 'POST' or request.method == 'post':
            batting_team = request.POST.get('batting_team')
            bowling_team = request.POST.get('bowling_team')
            city = request.POST.get('city')
            current_score = request.POST.get('current_score')
            current_over = request.POST.get('current_over')
            current_ball = request.POST.get('current_ball')
            wickets = request.POST.get('wickets')
            if not batting_team or not bowling_team or not city or not current_score or not current_over or not wickets:
                messages.success(request, "Given data is not correct!")
                return redirect('tournament:score-prediction-form')
            else:
                item = Tournament.objects.get(id=pk)
                pipe = pickle.load(open(item.score_prediction_model.path, 'rb'))

                balls = int(current_ball) + (round(int(current_over)) * 6)
                balls_left = 120 - int(balls)
                wickets = 10 - int(wickets)
                if balls == 0:
                    crr = 0.0
                else:
                    crr = round(((int(current_score) * 6) / int(balls)), 2)

                trf = ColumnTransformer([
                    ('trf', OneHotEncoder(sparse=False, drop='first'), ['batting_team', 'bowling_team', 'city'])
                ], remainder='passthrough')

                # runs_left = target - score
                # rrr = (runs_left * 6) / balls_left
                # input_df = pd.DataFrame(
                #     {'batting_team': ['Wellington'], 'bowling_team': ['Central Districts'], 'city': ['Auckland'],
                #      'current_score': [int(current_score)], 'balls_bowled': [int(balls)],
                #      'balls_left': [int(balls_left)], 'wickets_left': [int(wickets)], 'crr': [crr]})
                input_df = pd.DataFrame(
                    {'batting_team': ['Auckland'], 'bowling_team': ['Central Districts'], 'city': ['New Plymouth'],
                     'current_score': [170], 'balls_bowled': [108], 'balls_left': [12], 'wickets_left': [6],
                     'crr': [9.44]})
                ohe = trf.fit(input_df)
                df = ohe.transform(input_df)
                result = pipe.predict(df)[0]
                upper_limit = math.floor(result + current_score) - 8
                lower_limit = math.floor(result + current_score) + 4

                # math.floor(result)
                # print(
                #     'Probable Score: ' + str(math.floor(result + 170) - 8) + ' to ' + str(math.floor(result + 170) + 4))

                context = {
                    'upper_limit': str(upper_limit),
                    'lower_limit': str(lower_limit)
                }

                return render(request, 'userpanel/score_prediction_form.html', context)


class FirstWinPredictionView(TemplateView):
    def get(self, request, pk, *args):
        item = Tournament.objects.get(id=pk)
        teams = TeamName.objects.filter(tournament=item)
        venues = VenueName.objects.filter(tournament=item)

        context = {
            'tournament': item,
            'teams': teams,
            'venues': venues
        }

        return render(request, 'userpanel/first_innings_win_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.method == 'POST' or request.method == 'post':
            batting_team = request.POST.get('batting_team')
            bowling_team = request.POST.get('bowling_team')
            city = request.POST.get('city')
            total_score = request.POST.get('total_score')
            if not batting_team or not bowling_team or not city or not total_score:
                messages.success(request, "Given data is not correct!")
                return redirect('tournament:score-prediction-form')
            else:
                item = Tournament.objects.get(id=pk)
                pipe = pickle.load(open(item.first_innings_win_prediction_model.path, 'rb'))
                input_df = pd.DataFrame(
                    {'batting_team': ['Southern Vipers'], 'bowling_team': ['Western Storm'], 'city': ['Brighton'],
                     'runs_y': [190]})
                result = pipe.predict_proba(input_df)

                loss = result[0][1]
                win = result[0][0]

                pass


class SecondWinPredictionView(TemplateView):
    def get(self, request, pk, *args):
        item = Tournament.objects.get(id=pk)
        teams = TeamName.objects.filter(tournament=item)
        venues = VenueName.objects.filter(tournament=item)

        context = {
            'tournament': item,
            'teams': teams,
            'venues': venues
        }

        return render(request, 'userpanel/second_innings_win_form.html', context)

    def post(self, request, pk, *args, **kwargs):
        if request.method == 'POST' or request.method == 'post':
            batting_team = request.POST.get('batting_team')
            bowling_team = request.POST.get('bowling_team')
            city = request.POST.get('city')
            current_score = request.POST.get('current_score')
            running_overs = request.POST.get('current_over')
            wickets = request.POST.get('wickets')
            target_score = request.POST.get('target_score')
            if not batting_team or not bowling_team or not city or not current_score or not running_overs or not wickets or not target_score:
                messages.success(request, "Given data is not correct!")
                return redirect('tournament:score-prediction-form')
            else:
                item = Tournament.objects.get(id=pk)
                pipe = pickle.load(open(item.second_innings_win_prediction_model.path, 'rb'))
                input_df = pd.DataFrame(
                    {'batting_team': ['Peshawar Zalmi'], 'bowling_team': ['Quetta Gladiators'], 'city': ['Sharjah'],
                     'current_score': [159], 'target_runs': [169], 'runs_left': [10], 'balls_left': [2],
                     'wickets_left': [7], 'crr': [8.08], 'rrr': [30.0]})
                result = pipe.predict_proba(input_df)

                loss = result[0][0]
                win = result[0][1]
                pass


class DownloadView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userpanel/download.html')

    def post(self, request, *args, **kwargs):
        pass


class AboutUsView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'userpanel/aboutus.html')

    def post(self, request, *args, **kwargs):
        pass
