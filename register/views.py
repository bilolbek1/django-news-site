from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, View
from .models import Profile
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth.models import User

# Create your views here.

@login_required
def UserProfileView(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'profile': profile
    }
    return render(request, 'profile/user_profile.html', context)



class SignUpView(View):
    def get(self, request):
        user_form = UserRegistrationForm()
        context = {
            "user_form": user_form
        }
        return render(request, "registration/signup.html", context)

    def post(self, request):
        user_form = UserRegistrationForm(data=request.POST)

        if user_form.is_valid():
            user_form.save()

            return redirect('login')

        else:
            context = {
                'user_form': user_form
            }
            return render(request, 'registration/signup.html', context)

@login_required
def User_Edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST,
                                       files=request.FILES)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('user_profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }
        return render(request, 'profile/edit_profile.html', context)



