from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path
from .views import UserProfileView, SignUpView, User_Edit
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, \
PasswordResetCompleteView, PasswordResetDoneView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView, name='user_profile'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(), name='password-change-done'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name='password-reset-complete'),
    path('signup/', SignUpView, name='signup'),
    path('profile/edit', User_Edit, name='profile_edit'),
]
