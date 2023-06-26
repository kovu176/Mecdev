
from django.contrib import admin
from django.urls import path, include  
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from clientes.views import LandingView, SignupView, LandingQueryView

urlpatterns = [
    path('', LandingQueryView.as_view(), name='landing'),
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
