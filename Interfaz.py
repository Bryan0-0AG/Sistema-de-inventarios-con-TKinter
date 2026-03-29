import tkinter as tk
from tkinter import font
from Main import nuevo_inventario, nuevo_producto
from Visualización_deDatos import actualizar_visualizacion_datos

inv = nuevo_inventario("Frutas")
ventana = tk.Tk()
ventana.geometry("450x250")
output = tk.Label(ventana, text=""); output.grid(column=0, row=10)

# Añadir producto - ELEMENTOS
title1Label = tk.Label(ventana, text="Manejo de inventario 'Frutas'", font=font.Font(weight="bold")); title1Label.grid(column=0, row=0)
nombreLabel = tk.Label(ventana, text="Nombre"); nombreLabel.grid(column=0, row=1)
nombreInput = tk.Entry(ventana); nombreInput.grid(column=0, row=2)
precioLabel = tk.Label(ventana, text="Precio"); precioLabel.grid(column=0, row=3)
precioInput = tk.Entry(ventana); precioInput.grid(column=0, row=4)
cantidadLabel = tk.Label(ventana, text="Cantidad"); cantidadLabel.grid(column=0, row=5)
cantidadInput = tk.Entry(ventana); cantidadInput.grid(column=0, row=6)
# ------ EJECUTAR
def main(action):   
    def limpiarDatos():
        nombreInput.delete(0, tk.END)
        precioInput.delete(0, tk.END)
        cantidadInput.delete(0, tk.END)
    def inputError(errorMsg):
        limpiarDatos()
        output.config(text="Unknown error." if not errorMsg else errorMsg)
        ventana.after(2000, lambda: output.config(text=""))          
         
    # Obtenemos cada valor     
    nombre = nombreInput.get()
    try: cantidad = int(cantidadInput.get())
    except ValueError: cantidad = 0       
    try: precio = float(precioInput.get())
    except ValueError: precio = 0

    # Acciones
    new_product = nuevo_producto(nombre, precio)
    if action == "add": inv.añadirProducto(new_product, cantidad)
    elif action == "delete": inv.eliminarProducto(new_product)
    elif action == "updateC": 
        if cantidad != 0: inv.actualizarCantidad(new_product, cantidad, "C")
        else: inputError("Error: La cantidad debe ser un número diferente de 0."); return
    elif action == "updateP":
        if precio != 0: inv.actualizarCantidad(new_product, precio, "P")
        else: inputError("Error: El precio debe ser un número diferente de 0."); return
    elif action == "substract": 
        if cantidad != 0: inv.restarProducto(new_product, cantidad)
        else: inputError("Error: La cantidad debe ser un número diferente de 0."); return
    
    actualizar_visualizacion_datos(inv.ruta_excel)    
    limpiarDatos()
# ------ BOTONES
title2Label = tk.Label(ventana, text="Comandos", font=font.Font(weight="bold")); title2Label.grid(column=2, row=0)
add_boton = tk.Button(ventana, text="Añadir", command=lambda: main("add")); add_boton.grid(column=1, row=2)
del_boton = tk.Button(ventana, text="Eliminar", command=lambda: main("delete")); del_boton.grid(column=1, row=3)
updtC_boton = tk.Button(ventana, text="Actualizar cantidad", command=lambda: main("updateC")); updtC_boton.grid(column=2, row=2)
updtP_boton = tk.Button(ventana, text="Actualizar precio", command=lambda: main("updateP")); updtP_boton.grid(column=2, row=3)
subs_boton = tk.Button(ventana, text="Restar", command=lambda: main("substract")); subs_boton.grid(column=3, row=2)

ventana.mainloop()