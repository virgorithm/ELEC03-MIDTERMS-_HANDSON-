from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, AccountForm,CustomRegisterForm
from .models import Personal_Information
from django.views import View


   
def account(request):
    if request.method =='POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = AccountForm()
    return render(request, 'accountform.html', {'form':form})


# Register View
def register_user(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Personal_Information.objects.create(
                user=user,
                student_Id=form.cleaned_data.get('student_Id'),
                lrn=form.cleaned_data.get('lrn'),
                gender=form.cleaned_data.get('gender'),
                phone_number=form.cleaned_data.get('phone_number'),
                address=form.cleaned_data.get('address')
            )
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login_user')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# Login View
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid input.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Logout View
def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login_user', )


def PersonalInfo(request):
    if request.method =='POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'students/success.html')
    else:
        form = CustomRegisterForm()
    return render(request, 'students/enroll.html', {'form':form})

#dashboard

from django.contrib.auth.decorators import login_required

@login_required(login_url='login_user')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def profile_view(request):
    return render(request, 'accounts/profile.html')



