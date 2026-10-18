"""Geohash encoding and decoding of geographic coordinates."""

from typing import Tuple

BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"
BASE32_MAP = {c: i for i, c in enumerate(BASE32)}


def encode_geohash(latitude: float, longitude: float, precision: int = 10) -> str:
    """Encode latitude and longitude into Geohash string."""
    lat_interval = [-90.0, 90.0]
    lon_interval = [-180.0, 180.0]

    geohash = []
    bits = [16, 8, 4, 2, 1]
    bit = 0
    ch = 0
    is_even = True

    while len(geohash) < precision:
        if is_even:
            mid = (lon_interval[0] + lon_interval[1]) / 2.0
            if longitude > mid:
                ch |= bits[bit]
                lon_interval[0] = mid
            else:
                lon_interval[1] = mid
        else:
            mid = (lat_interval[0] + lat_interval[1]) / 2.0
            if latitude > mid:
                ch |= bits[bit]
                lat_interval[0] = mid
            else:
                lat_interval[1] = mid

        is_even = not is_even
        if bit < 4:
            bit += 1
        else:
            geohash.append(BASE32[ch])
            bit = 0
            ch = 0

    return "".join(geohash)


def decode_geohash(geohash: str) -> Tuple[float, float]:
    """Decode Geohash string into latitude and longitude tuple."""
    lat_interval = [-90.0, 90.0]
    lon_interval = [-180.0, 180.0]
    is_even = True

    for c in geohash.lower():
        cd = BASE32_MAP.get(c)
        if cd is None:
            raise ValueError(f"Invalid geohash character: '{c}'")
        for mask in [16, 8, 4, 2, 1]:
            if is_even:
                mid = (lon_interval[0] + lon_interval[1]) / 2.0
                if cd & mask:
                    lon_interval[0] = mid
                else:
                    lon_interval[1] = mid
            else:
                mid = (lat_interval[0] + lat_interval[1]) / 2.0
                if cd & mask:
                    lat_interval[0] = mid
                else:
                    lat_interval[1] = mid
            is_even = not is_even

    lat = (lat_interval[0] + lat_interval[1]) / 2.0
    lon = (lon_interval[0] + lon_interval[1]) / 2.0
    return round(lat, 5), round(lon, 5)
