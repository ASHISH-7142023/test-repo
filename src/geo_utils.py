"""Geographical calculations: Haversine distance, coordinate sanity checks, and bearing."""

import math
from typing import Tuple


def is_valid_coordinates(latitude: float, longitude: float) -> bool:
    """Validate latitude (-90 to 90) and longitude (-180 to 180) ranges."""
    try:
        lat = float(latitude)
        lon = float(longitude)
        return -90.0 <= lat <= 90.0 and -180.0 <= lon <= 180.0
    except (ValueError, TypeError):
        return False


def haversine_distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great-circle distance between two geographic points
    on the Earth surface using the Haversine formula in kilometers.
    """
    if not (is_valid_coordinates(lat1, lon1) and is_valid_coordinates(lat2, lon2)):
        raise ValueError("Invalid GPS coordinates provided.")

    r = 6371.0  # Earth mean radius in km
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)

    a = (math.sin(d_lat / 2.0) ** 2 +
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
         math.sin(d_lon / 2.0) ** 2)
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return round(r * c, 3)


def calculate_bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate the initial compass bearing in degrees (0-360) from point 1 to point 2."""
    if not (is_valid_coordinates(lat1, lon1) and is_valid_coordinates(lat2, lon2)):
        raise ValueError("Invalid GPS coordinates.")

    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_lambda = math.radians(lon2 - lon1)

    y = math.sin(delta_lambda) * math.cos(phi2)
    x = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(delta_lambda)
    theta = math.atan2(y, x)
    bearing = (math.degrees(theta) + 360.0) % 360.0
    return round(bearing, 2)
