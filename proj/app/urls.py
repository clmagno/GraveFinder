from django.urls import path,include
from . import views
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from rest_framework import routers
from .views import UserViewSet, LoginAPIView
from .views import CustomTokenObtainPairView
app_name = 'app'
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
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
    path('api/', include(router.urls)),
    path('users/login/', LoginAPIView.as_view(), name='login'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', views.register, name='register'),


]



