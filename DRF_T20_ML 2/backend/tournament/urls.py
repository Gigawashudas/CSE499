from django.urls import path
from tournament import views

app_name = 'tournament'
urlpatterns = [
    path('', views.HomeListView.as_view(), name='index'),
    path('download/', views.DownloadView.as_view(), name='download'),
]
