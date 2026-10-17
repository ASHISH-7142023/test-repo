import unittest
import math
from src.vector3d import Vector3D

class TestVector3D(unittest.TestCase):
    def test_arithmetic(self):
        v1 = Vector3D(1.0, 2.0, 3.0)
        v2 = Vector3D(4.0, 5.0, 6.0)
        self.assertEqual(v1 + v2, Vector3D(5.0, 7.0, 9.0))
        self.assertEqual(v2 - v1, Vector3D(3.0, 3.0, 3.0))
        self.assertEqual(v1 * 2, Vector3D(2.0, 4.0, 6.0))

    def test_dot_and_cross(self):
        i = Vector3D(1.0, 0.0, 0.0)
        j = Vector3D(0.0, 1.0, 0.0)
        self.assertEqual(i.dot(j), 0.0)
        self.assertEqual(i.cross(j), Vector3D(0.0, 0.0, 1.0))

    def test_magnitude_and_distance(self):
        v = Vector3D(3.0, 4.0, 0.0)
        self.assertEqual(v.magnitude(), 5.0)
        self.assertEqual(v.normalize(), Vector3D(0.6, 0.8, 0.0))
        self.assertAlmostEqual(v.angle_with(Vector3D(0.0, 1.0, 0.0)), math.acos(0.8))

if __name__ == "__main__":
    unittest.main()
