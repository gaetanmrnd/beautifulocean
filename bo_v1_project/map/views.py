from django.shortcuts import render

def mapframe(request):
    return render(request, 'map/background.html', {})