from django.urls import path
from tournament import views

app_name = 'tournament'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('score-prediction/<int:pk>/', views.ScorePredictionView.as_view(), name='score-prediction-form'),
    path('first-innings-prediction/<int:pk>/', views.FirstWinPredictionView.as_view(), name='first-prediction-form'),
    path('second-innings-prediction/<int:pk>/', views.SecondWinPredictionView.as_view(), name='second-prediction-form'),
    path('download/', views.DownloadView.as_view(), name='download'),
    path('about-us/', views.AboutUsView.as_view(), name='about_us'),
]
