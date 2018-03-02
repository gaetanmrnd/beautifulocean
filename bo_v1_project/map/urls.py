from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wrecks/', views.wrecks, name='wrecks'),
    url(r'^', views.mapframe, name='mapframe'),
]