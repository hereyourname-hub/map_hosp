import location as location
from django.shortcuts import render
from .models import Location
import folium
from folium.plugins import FastMarkerCluster

# Create your views here.
def home(request):
    locations = Location.objects.all()
    initialMap = folium.Map(location=[41.2611204525265, 74.61809829460819], zoom_start=8)

    data = []


    marker_cluster = FastMarkerCluster(data).add_to(initialMap)

    for location in locations:
        folium.Marker(location=[location.lat, location.lng], popup='Филиал больницы: ' + location.name).add_to(marker_cluster)

    context = {'map':initialMap._repr_html_(), 'locations':locations}
    return render(request, 'map/home.html', context)
