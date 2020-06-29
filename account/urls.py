from django.urls import path
from .views import logout_view, login_view, update_user_view, violation_view
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('violation/', violation_view, name="violations_url"),
    path('logout/', logout_view, name="logout"),
    path('user_profile/', update_user_view, name="user_profile_url"),
    path('register/', update_user_view, name="user_profile_url"),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
