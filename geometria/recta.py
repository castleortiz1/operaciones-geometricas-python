from .punto import Punto

class Recta:
    def __init__(self, punto1, punto2):
        self.punto1 = punto1
        self.punto2 = punto2

    def pendiente(self):
        return (self.punto2.y - self.punto1.y) / (self.punto2.x - self.punto1.x)

    def __repr__(self):
        return f"Recta({self.punto1}, {self.punto2})"
