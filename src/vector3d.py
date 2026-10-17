"""3D Vector mathematics dataclass."""

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Vector3D:
    """Immutable 3D spatial vector with geometric operations."""

    x: float
    y: float
    z: float

    def __add__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar: float) -> "Vector3D":
        return Vector3D(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar: float) -> "Vector3D":
        return self * scalar

    def __truediv__(self, scalar: float) -> "Vector3D":
        if scalar == 0:
            raise ZeroDivisionError("Cannot divide vector by zero.")
        return Vector3D(self.x / scalar, self.y / scalar, self.z / scalar)

    def dot(self, other: "Vector3D") -> float:
        """Compute the dot product."""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: "Vector3D") -> "Vector3D":
        """Compute the vector cross product."""
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def magnitude(self) -> float:
        """Calculate vector Euclidean length (L2 norm)."""
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self) -> "Vector3D":
        """Return unit vector with magnitude 1.0."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return self / mag

    def distance_to(self, other: "Vector3D") -> float:
        """Calculate Euclidean distance between two points."""
        return (self - other).magnitude()

    def angle_with(self, other: "Vector3D") -> float:
        """Return angle between two vectors in radians."""
        dot_p = self.dot(other)
        mags = self.magnitude() * other.magnitude()
        if mags == 0:
            raise ValueError("Cannot calculate angle with zero vector.")
        cos_theta = max(-1.0, min(1.0, dot_p / mags))
        return math.acos(cos_theta)
