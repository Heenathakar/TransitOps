from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import UserProfile

def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name or user.username}!")
            return redirect("dashboard")
        
        messages.error(request, "Invalid Username or Password")
        return render(request, "login.html", {"form": form})

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

@login_required
def dashboard(request):
    # Ensure profile exists
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user, role='admin' if request.user.is_superuser else 'driver')
    
    role = request.user.profile.role
    
    # Mock data depending on the role to demonstrate RBAC
    stats = {}
    if role == 'admin':
        stats = {
            'card_1_title': 'Total Accounts', 'card_1_val': '24', 'card_1_icon': 'fas fa-users-cog',
            'card_2_title': 'System Uptime', 'card_2_val': '99.98%', 'card_2_icon': 'fas fa-server',
            'card_3_title': 'Active Sessions', 'card_3_val': '7', 'card_3_icon': 'fas fa-user-clock',
            'card_4_title': 'Security Alerts', 'card_4_val': '0', 'card_4_icon': 'fas fa-shield-alt',
        }
    elif role == 'manager':
        stats = {
            'card_1_title': 'Total Vehicles', 'card_1_val': '45', 'card_1_icon': 'fas fa-bus',
            'card_2_title': 'Active Drivers', 'card_2_val': '32', 'card_2_icon': 'fas fa-id-card',
            'card_3_title': 'Maintenance Alerts', 'card_3_val': '3', 'card_3_icon': 'fas fa-tools',
            'card_4_title': 'Monthly Mileage', 'card_4_val': '12,450 km', 'card_4_icon': 'fas fa-road',
        }
    elif role == 'dispatcher':
        stats = {
            'card_1_title': 'Active Routes', 'card_1_val': '18', 'card_1_icon': 'fas fa-route',
            'card_2_title': 'Pending Dispatches', 'card_2_val': '5', 'card_2_icon': 'fas fa-clock',
            'card_3_title': 'Completed Trips (Today)', 'card_3_val': '42', 'card_3_icon': 'fas fa-check-circle',
            'card_4_title': 'Available Drivers', 'card_4_val': '8', 'card_4_icon': 'fas fa-user-check',
        }
    else:  # driver
        stats = {
            'card_1_title': 'My Shift Status', 'card_1_val': 'On Duty', 'card_1_icon': 'fas fa-business-time',
            'card_2_title': 'Assigned Trips (Today)', 'card_2_val': '3', 'card_2_icon': 'fas fa-route',
            'card_3_title': 'Completed Trips', 'card_3_val': '158', 'card_3_icon': 'fas fa-award',
            'card_4_title': 'Vehicle Status', 'card_4_val': 'Perfect', 'card_4_icon': 'fas fa-check-shield',
        }

    context = {
        'stats': stats,
        'role_display': request.user.profile.get_role_display(),
    }
    return render(request, "dashboard.html", context)

@login_required
def profile_view(request):
    # Ensure profile exists
    if not hasattr(request.user, 'profile'):
        UserProfile.objects.create(user=request.user)

    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, "Your profile details have been successfully updated!")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form,
        "role_display": request.user.profile.get_role_display(),
    }
    return render(request, "profile.html", context)

def logout_view(request):
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect("login")