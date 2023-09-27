from django.urls import path
from account import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.Userlogin, name='login'),
    path('forgot-password/', views.ForgotPassword, name='forgot-password'),
    path('change-password/<token>/', views.ChangePassword, name='change-password'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile-form/', views.ProfileForm.as_view(), name='profile-form'),
    path('logout/', views.LogoutPage, name='logout'),
]
