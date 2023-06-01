from django.urls import path
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name = 'app'

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='app/login.html',
        success_url=reverse_lazy('app:dashboard')
    ), name='login'),

    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reservation/', views.reservation, name='reservation'), 
    path('map/', views.map, name='map'),
    path('navigation/', views.navigation, name='navigation'),



]



