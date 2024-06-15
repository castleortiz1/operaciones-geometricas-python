# main.py
from geometria.punto import Punto
from geometria.recta import Recta
from geometria.vector import Vector

def distancia_entre_puntos(punto1, punto2):
    import math
    return math.sqrt((punto2.x - punto1.x) ** 2 + (punto2.y - punto1.y) ** 2)

def main():
    # Crear puntos
    punto1 = Punto(1, 2)
    punto2 = Punto(4, 6)

    # Calcular distancia entre puntos
    distancia = distancia_entre_puntos(punto1, punto2)
    print("Distancia entre los puntos:", distancia)

    # Crear recta
    recta = Recta(punto1, punto2)

    # Calcular pendiente de la recta
    pendiente = recta.pendiente()
    print("Pendiente de la recta:", pendiente)

    # Crear vectores
    vector1 = Vector(3, 4)
    vector2 = Vector(5, 6)

    # Calcular producto punto
    producto = vector1.producto_punto(vector2)
    print("Producto punto entre los vectores:", producto)

if __name__ == "__main__":
    main()
