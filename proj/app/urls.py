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
    path('login/', views.login_view, name='login'),  # Updated login URL mapping

    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('reservation/', views.reservation, name='reservation'),
    path('map/', views.map, name='map'),
    path('navigation/', views.navigation, name='navigation'),
    path('api/', include(router.urls)),

    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/register/', views.register, name='api_register'),  # Renamed to avoid conflict with register view
]


