import unittest
from geometria.punto import Punto
from geometria.recta import Recta
from geometria.vector import Vector

class TestGeometria(unittest.TestCase):
    
    def test_punto(self):
        punto = Punto(1, 2)
        self.assertEqual(punto.x, 1)
        self.assertEqual(punto.y, 2)
    
    def test_recta(self):
        punto1 = Punto(1, 2)
        punto2 = Punto(4, 6)
        recta = Recta(punto1, punto2)
        self.assertAlmostEqual(recta.pendiente(), 1.3333333, places=7)
    
    def test_vector_producto_punto(self):
        vector1 = Vector(3, 4)
        vector2 = Vector(5, 6)
        self.assertEqual(vector1.producto_punto(vector2), 39)
    
    def test_vector_producto_cruz(self):
        vector1 = Vector(3, 4)
        vector2 = Vector(5, 6)
        self.assertEqual(vector1.producto_cruz(vector2), -2)

if __name__ == '__main__':
    unittest.main()
