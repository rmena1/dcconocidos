from django.urls import path
from . import views

app_name = 'user_manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register_user, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
]