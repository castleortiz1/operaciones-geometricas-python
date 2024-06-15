import tkinter as tk
from tkinter import messagebox
from geometria.punto import Punto
from geometria.recta import Recta
from geometria.vector import Vector

def distancia_entre_puntos(punto1, punto2):
    import math
    return math.sqrt((punto2.x - punto1.x) ** 2 + (punto2.y - punto1.y) ** 2)

class GeometriaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Operaciones Geométricas")

        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y entradas para Punto 1
        tk.Label(self.root, text="Punto 1").grid(row=0, column=0, pady=10)
        tk.Label(self.root, text="x1:").grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.root, text="y1:").grid(row=2, column=0, sticky=tk.E)
        self.x1_entry = tk.Entry(self.root)
        self.y1_entry = tk.Entry(self.root)
        self.x1_entry.grid(row=1, column=1)
        self.y1_entry.grid(row=2, column=1)

        # Etiquetas y entradas para Punto 2
        tk.Label(self.root, text="Punto 2").grid(row=0, column=2, pady=10)
        tk.Label(self.root, text="x2:").grid(row=1, column=2, sticky=tk.E)
        tk.Label(self.root, text="y2:").grid(row=2, column=2, sticky=tk.E)
        self.x2_entry = tk.Entry(self.root)
        self.y2_entry = tk.Entry(self.root)
        self.x2_entry.grid(row=1, column=3)
        self.y2_entry.grid(row=2, column=3)

        # Botón para calcular la distancia
        tk.Button(self.root, text="Calcular Distancia", command=self.calcular_distancia).grid(row=3, column=0, columnspan=4, pady=20)

        # Etiquetas y entradas para Vectores
        tk.Label(self.root, text="Vector 1").grid(row=4, column=0, pady=10)
        tk.Label(self.root, text="x1:").grid(row=5, column=0, sticky=tk.E)
        tk.Label(self.root, text="y1:").grid(row=6, column=0, sticky=tk.E)
        self.v1x_entry = tk.Entry(self.root)
        self.v1y_entry = tk.Entry(self.root)
        self.v1x_entry.grid(row=5, column=1)
        self.v1y_entry.grid(row=6, column=1)

        tk.Label(self.root, text="Vector 2").grid(row=4, column=2, pady=10)
        tk.Label(self.root, text="x2:").grid(row=5, column=2, sticky=tk.E)
        tk.Label(self.root, text="y2:").grid(row=6, column=2, sticky=tk.E)
        self.v2x_entry = tk.Entry(self.root)
        self.v2y_entry = tk.Entry(self.root)
        self.v2x_entry.grid(row=5, column=3)
        self.v2y_entry.grid(row=6, column=3)

        # Botón para calcular el producto punto
        tk.Button(self.root, text="Calcular Producto Punto", command=self.calcular_producto_punto).grid(row=7, column=0, columnspan=4, pady=20)

    def calcular_distancia(self):
        try:
            x1 = float(self.x1_entry.get())
            y1 = float(self.y1_entry.get())
            x2 = float(self.x2_entry.get())
            y2 = float(self.y2_entry.get())
            punto1 = Punto(x1, y1)
            punto2 = Punto(x2, y2)
            distancia = distancia_entre_puntos(punto1, punto2)
            messagebox.showinfo("Resultado", f"Distancia: {distancia}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

    def calcular_producto_punto(self):
        try:
            v1x = float(self.v1x_entry.get())
            v1y = float(self.v1y_entry.get())
            v2x = float(self.v2x_entry.get())
            v2y = float(self.v2y_entry.get())
            vector1 = Vector(v1x, v1y)
            vector2 = Vector(v2x, v2y)
            producto = vector1.producto_punto(vector2)
            messagebox.showinfo("Resultado", f"Producto Punto: {producto}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometriaApp(root)
    root.mainloop()
