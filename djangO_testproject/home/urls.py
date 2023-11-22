from django.urls import path

from . import views
from .views import CreateActivityView


urlpatterns = [ 
    path('', views.HomeView.as_view(), name='home'),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('create_activity/', CreateActivityView.as_view(), name='create_activity'),
]