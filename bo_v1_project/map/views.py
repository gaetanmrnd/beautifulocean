from django.shortcuts import render
from .models import Obstacle
import json

def mapframe(request):
    return render(request, 'map/background.html', {})

def wrecks(request):
	wrecks = Obstacle.objects.filter(obstacle_type = 0)
	return render(request, 'map/background.html', {'wrecks': wrecks})