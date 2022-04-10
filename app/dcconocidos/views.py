from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Location

def index(request):
    if request.user.is_authenticated:
        locations = request.user.location_set.all()
        other_locations = Location.objects.exclude(user=request.user)
    else:
        locations = None
        other_locations = None
    return render(request, 'dcconocidos/index.html', {'locations': locations, 'other_locations':other_locations})

def add_spot(request):
    if request.method == 'POST':
        lng = request.POST['lng']
        lat = request.POST['lat']
        return render(request, 'dcconocidos/add_spot.html', {'lng':lng, 'lat':lat})

def create_new_location(request):
    if request.method == 'POST':
        lng = request.POST['lng']
        lat = request.POST['lat']
        name = request.POST['loc_name']
        new_location = Location(latitude=lat, longitude=lng, location_name=name, user=request.user)
        new_location.save()
    return redirect('/')
