from django.urls import path, include
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='login', permanent=True)),
    path('profile/', views.profile, name='profile'),
    path('logged_out/', views.logged_out, name='logged_out'),
    path('register/', views.register, name='register'),
]