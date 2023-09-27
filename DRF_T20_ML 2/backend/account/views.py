from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from account import models

from account.forms import RegistrationForm, ProfileForm

# authentication functions
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import uuid

from account.models import Profile
from account.helpers import send_forgot_password_mail

from django.views.generic import TemplateView

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def register(request):
    if request.user.is_authenticated:
        return redirect('tournament:index')
    else:
        if request.method == 'post' or request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Account has been created!")
                return render(request, 'login.html')
        else:
            form = RegistrationForm()

    context = {
        'form': form
    }
    return render(request, 'register.html', context)


def Userlogin(request):
    if request.user.is_authenticated:
        return redirect('tournament:index')
    else:
        if request.method == 'POST' or request.method == 'post':
            email = request.POST.get('email')
            password = request.POST.get('password')
            customer = authenticate(email=email, password=password)
            if customer is not None:
                login(request, customer)
                return redirect('tournament:index')
            else:
                messages.success(request, "Email or Password is incorrect!")
                return render(request, 'login.html')

    return render(request, 'login.html')


def ForgotPassword(request):
    try:
        if request.method == 'POST' or request.method == 'post':
            email = request.POST.get('email')
            if not User.objects.filter(email=email).first():
                messages.success(request, "Email not exist!")
                return redirect(request, 'account:register')
            else:
                token = str(uuid.uuid4())
                user_obj = User.objects.get(email=email)
                user_obj.forgot_password_token = token
                user_obj.save()
                send_forgot_password_mail(email=email, token=token)
                messages.success(request, "A password reset link sent to your email!")
                return redirect(request, 'account:forgot-password')

    except Exception as e:
        print(e)

    return render(request, 'forgot_password.html')


def ChangePassword(request, token):
    context = {}
    try:
        user_obj = User.objects.filter(forgot_password_token=token).first()
        context = {'user_id': user_obj.id}

        if request.method == 'post' or request.method == 'POST':
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, "No user found!")
                return redirect(request, f'change-password/{token}/')
            if pass1 != pass2:
                messages.success(request, "Your password and confirm password are not Same!")
                return redirect(request, f'change-password/{token}/')

            user_pass_obj = User.objects.get(id=user_id)
            user_pass_obj.set_password(pass1)
            user_pass_obj.save()
            return redirect(request, 'account:login')

    except Exception as e:
        print(e)

    return render(request, 'change_password.html', context)


def LogoutPage(request):
    logout(request)
    return redirect('account:login')


class ProfileView(TemplateView):
    def get(self, request, *args, **kwargs):

        profile_obj = Profile.objects.get(user=request.user)
        context = {
            'profile': profile_obj,
        }
        return render(request, 'profile.html', context)

    def post(self, request, *args, **kwargs):
        pass


class ProfileForm(TemplateView):
    def get(self, request, *args, **kwargs):

        profile_obj = Profile.objects.get(user=request.user)
        profileForm = ProfileForm(instance=profile_obj)

        context = {
            'profileForm': profileForm,
        }
        return render(request, 'profile_form.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile has been updated!")
                return render(request, 'profile.html')
            else:
                form = ProfileForm()

            context = {
                'form': form
            }
            return render(request, 'profile_form.html', context)

