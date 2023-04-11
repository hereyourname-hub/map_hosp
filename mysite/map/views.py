from django.shortcuts import render
from .models import Location
import folium
from folium.plugins import FastMarkerCluster

# Create your views here.
def home(request):
    locations = Location.objects.all()
    initialMap = folium.Map(location=[41.2611204525265, 74.61809829460819], zoom_start=8)

    lat = [location.lat for location in locations]
    long = [location.lng for location in locations]

    print(lat)
    print(long)
    print(list(zip(lat,long)))

    FastMarkerCluster(data=zip(lat,long)).add_to(initialMap)

 #   for location in locations:
 #       coordinates = (location.lat, location.lng)
 #       folium.Marker(coordinates, popup='Филиал больницы:  ' + location.name).add_to(initialMap)


    context = {'map':initialMap._repr_html_(), 'locations':locations}
    return render(request, 'map/home.html', context)

