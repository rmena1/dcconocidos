from django.urls import path

from . import views

app_name = 'dcconocidos'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_spot', views.add_spot, name='add_spot'),
    path('create_new_location', views.create_new_location, name='create_new_location'),
]