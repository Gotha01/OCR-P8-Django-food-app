from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import View

from . import forms

class LoginPageView(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(
            request,
            self.template_name,
            context={'form': form, 'message':message}
            )

    def post(self, request):
        form = self.form_class(request.POST)
        message = ""
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
                )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                message = 'Identifiants invalides.'
        return render(
            request,
            self.template_name,
            context={'form': form, 'message':message}
            ) 

def logout_user(request):
    logout(request)
    return redirect('home')

def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(
        request,
        'authentication/signup.html',
        context={'form':form}
        )

@login_required
def profile_page(request):
    return render(request,'authentication/profile_page.html')

@login_required
def change_profile(request):
    user = request.user
    form = forms.ModifyUser(request.POST or None, initial={'username': user.username, 'email': user.email})
    if request.method == 'POST':
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('profile_page')
    return render(request, 'authentication/modify_user.html', {'form': form})