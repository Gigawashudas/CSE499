from django.urls import path
from dashboard import views

app_name = 'dashboard'
urlpatterns = [
    path('index/', views.DashboardIndexView.as_view(), name='dashboard_index'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('tournaments/', views.TournamentListView.as_view(), name='tournaments'),
    path('tournaments/add-new/', views.AddNewTournament.as_view(), name='add_new_tournament'),
    path('tournaments/<int:pk>/', views.TournamentUpdateView.as_view(), name='tournament_update'),
    path('tournaments/delete/<int:pk>/', views.TournamentDeleteView.as_view(), name='tournament_delete'),
    path('teams/', views.TeamListView.as_view(), name='teams'),
    path('teams/add-new/', views.AddNewTeamName.as_view(), name='add_new_team'),
    path('teams/<int:pk>/', views.TeamNameUpdateView.as_view(), name='team_update'),
    path('teams/delete/<int:pk>/', views.TeamNameDeleteView.as_view(), name='team_delete'),
    path('venues/', views.VenueListView.as_view(), name='venues'),
    path('venues/add-new/', views.AddNewVenue.as_view(), name='add_new_venue'),
    path('venues/<int:pk>/', views.VenueNameUpdateView.as_view(), name='venue_update'),
    path('venues/delete/<int:pk>/', views.VenueNameDeleteView.as_view(), name='venue_delete'),
    path('faqs/', views.FAQListView.as_view(), name='faq_list'),
    path('faqs/add-new/', views.AddNewFAQ.as_view(), name='add_new_faq'),
    path('faqs/<int:pk>/', views.FAQUpdateView.as_view(), name='faq_update'),
    path('faqs/delete/<int:pk>/', views.FAQDeleteView.as_view(), name='faq_delete'),
]
