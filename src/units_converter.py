"""Comprehensive metric and imperial unit conversion utilities."""

LENGTH_TO_METERS = {
    "m": 1.0, "km": 1000.0, "cm": 0.01, "mm": 0.001,
    "mi": 1609.344, "yd": 0.9144, "ft": 0.3048, "in": 0.0254,
}

WEIGHT_TO_GRAMS = {
    "g": 1.0, "kg": 1000.0, "mg": 0.001,
    "lb": 453.59237, "oz": 28.349523125,
}

BYTES_MAP = {
    "b": 1, "kb": 1024, "mb": 1024**2, "gb": 1024**3, "tb": 1024**4,
}


def convert_length(val: float, from_u: str, to_u: str) -> float:
    """Convert length between metric and imperial units."""
    f, t = from_u.lower(), to_u.lower()
    if f not in LENGTH_TO_METERS or t not in LENGTH_TO_METERS:
        raise ValueError(f"Unsupported length units: {from_u} -> {to_u}")
    meters = val * LENGTH_TO_METERS[f]
    return meters / LENGTH_TO_METERS[t]


def convert_weight(val: float, from_u: str, to_u: str) -> float:
    """Convert weight between metric and imperial units."""
    f, t = from_u.lower(), to_u.lower()
    if f not in WEIGHT_TO_GRAMS or t not in WEIGHT_TO_GRAMS:
        raise ValueError(f"Unsupported weight units: {from_u} -> {to_u}")
    grams = val * WEIGHT_TO_GRAMS[f]
    return grams / WEIGHT_TO_GRAMS[t]


def convert_temperature(val: float, from_u: str, to_u: str) -> float:
    """Convert temperature between Celsius (C), Fahrenheit (F), and Kelvin (K)."""
    f, t = from_u.upper(), to_u.upper()
    if f == t:
        return val
    if f == "C":
        c = val
    elif f == "F":
        c = (val - 32) * 5 / 9
    elif f == "K":
        c = val - 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {from_u}")

    if t == "C":
        return c
    elif t == "F":
        return c * 9 / 5 + 32
    elif t == "K":
        return c + 273.15
    else:
        raise ValueError(f"Unknown temperature unit: {to_u}")


def convert_bytes(val: float, from_u: str, to_u: str) -> float:
    """Convert digital storage units (B, KB, MB, GB, TB)."""
    f, t = from_u.lower(), to_u.lower()
    if f not in BYTES_MAP or t not in BYTES_MAP:
        raise ValueError(f"Unknown bytes unit: {from_u} -> {to_u}")
    total_bytes = val * BYTES_MAP[f]
    return total_bytes / BYTES_MAP[t]
