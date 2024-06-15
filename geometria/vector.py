class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def producto_punto(self, otro_vector):
        return self.x * otro_vector.x + self.y * otro_vector.y

    def producto_cruz(self, otro_vector):
        return self.x * otro_vector.y - self.y * otro_vector.x

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
