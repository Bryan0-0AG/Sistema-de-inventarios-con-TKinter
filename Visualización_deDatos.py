import tkinter as tk
import pandas as pd

ventana = tk.Tk()
ventana.geometry("175x500")

nombreLabel = tk.Label(ventana, text=("Nombre")); nombreLabel.grid(column=0, row=0)
precioLabel = tk.Label(ventana, text=("Precio")); precioLabel.grid(column=1, row=0)
cantidadLabel = tk.Label(ventana, text=("Cantidad")); cantidadLabel.grid(column=2, row=0)

widgetsGrid = []
def limpiar_grid():
    for fila in widgetsGrid:
        for widget in fila:
            widget.destroy()
    widgetsGrid.clear()   

def actualizar_visualizacion_datos(ruta_archivo_excel):
    global fila_final
    limpiar_grid()
    df = pd.read_excel(ruta_archivo_excel)
    for i, fila in df.iterrows():
        index = i +1
        nombre = fila['nombre']
        precio = fila['precio']
        cantidad = fila['cantidad']
        producto_nameLabel = tk.Label(ventana, text=(nombre)); producto_nameLabel.grid(column=0, row=index)
        producto_precioLabel = tk.Label(ventana, text=(str(precio))); producto_precioLabel.grid(column=1, row=index)
        producto_cantidadLabel = tk.Label(ventana, text=(str(cantidad))); producto_cantidadLabel.grid(column=2, row=index)
        list.append(widgetsGrid, [producto_nameLabel, producto_precioLabel, producto_cantidadLabel])