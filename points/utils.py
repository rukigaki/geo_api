from django.contrib.gis.geos import Point as GeoPoint
from django.contrib.gis.measure import D

from .models import Point

def get_points_in_radius(request, default_radius_km=1):
    try:
        lat = float(request.query_params["latitude"])
        lon = float(request.query_params["longitude"])
        radius_km = float(request.query_params.get("radius", default_radius_km))
    except (KeyError, ValueError):
        return Point.objects.none()

    center = GeoPoint(lon, lat)
    radius_m = radius_km * 1000

    return Point.objects.filter(location__distance_lte=(center, D(m=radius_m)))