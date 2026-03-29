import pandas as pd
import os

class nuevo_producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
   
class nuevo_inventario:
    def __init__(self, nombre):
        self.nombre = nombre
    
        root = os.path.dirname(os.path.abspath(__file__))

        carpeta = os.path.join(root, "Inventarios")
        os.makedirs(carpeta, exist_ok=True)
    
        self.ruta_excel = os.path.join(carpeta, f"Inventario_{nombre}.xlsx") 

        if os.path.exists(self.ruta_excel): self.excel = pd.read_excel(self.ruta_excel)
        else:
            self.excel = pd.DataFrame(columns=["nombre", "precio", "cantidad"])
            self.excel.to_excel(self.ruta_excel, index=False)
    
    def añadirProducto(self, producto, cantidad):
        fila = self.excel.loc[self.excel["nombre"] == producto.nombre]
        newdata = [producto.nombre, producto.precio, max(1, cantidad)]

        if not fila.empty:
            self.excel.loc[self.excel["nombre"] == producto.nombre, "cantidad"] += cantidad
        else:
            self.excel.loc[len(self.excel)] = newdata
        self.excel.to_excel(self.ruta_excel, index=False)
        print(f"¡Se añadieron {cantidad} {producto.nombre}(s) exitosamente!")          
          
    def restarProducto(self, producto, cantidad_paraRestar):
        fila = self.excel.loc[self.excel["nombre"] == producto.nombre]
        
        if not fila.empty:
            nombre = fila["nombre"].values[0]
            cantidad = fila["cantidad"].values[0]
            restar = "default"
            
            if cantidad < cantidad_paraRestar:
                print(f"Solo hay {cantidad} {nombre}(s) y deseas eliminar {cantidad_paraRestar}.")
                try: restar = int(input(("¿Desea eliminarlos todos? Digite 1 para un sí, cualquier cosa para un no. ")))
                except ValueError: print("Cancelando operación."); return
                if restar != 1: print("Cancelando operación."); return
                
            if restar == 1 or restar == "default": # Restamos la cantidad
                nueva_cantidad = max(0, cantidad - cantidad_paraRestar)               
                self.excel.loc[self.excel["nombre"] == producto.nombre, "cantidad"] = nueva_cantidad
                print(f"¡Se eliminaron {cantidad_paraRestar} {nombre}(s) correctamente!...")
                self.excel.to_excel(self.ruta_excel, index=False)
        else: print("Producto no encontrado.")            
                
    def eliminarProducto(self, producto):
        fila = self.excel.loc[self.excel["nombre"] == producto.nombre]
        if not fila.empty:
            self.excel = self.excel.drop(fila.index)
            self.excel.reset_index(drop=True, inplace=True)
            self.excel.to_excel(self.ruta_excel, index=False)
        else: print("Producto no encontrado.")
                        
    def actualizarCantidad(self, producto, valor, accion):
        fila = self.excel.loc[self.excel["nombre"] == producto.nombre]
        if not fila.empty:
            anterior_valor = valor
            self.excel.loc[self.excel["nombre"] == producto.nombre, "cantidad" if accion == "C" else "precio"] = valor
            self.excel.to_excel(self.ruta_excel, index=False)
            
            valor_en_excel = self.excel.loc[self.excel["nombre"] == producto.nombre, "cantidad" if accion == "C" else "precio"].values[0]
            print(f"¡Se actualizó {"la" if accion == "C" else "el"} {"cantidad" if accion == "C" else "precio"} de {producto.nombre} de {anterior_valor} a {valor_en_excel} correctamente!...")
        else: print("Producto no encontrado.")        
            
    def buscarProducto(self, producto):
        fila = self.excel.loc[self.excel["nombre"]]
        if not fila.empty:
            nombre = fila["nombre"].values[0]
            cantidad = fila["cantidad"].values[0]
            print(f"Se encontró {cantidad} {nombre}(s) en el inventario.")
            return True
        else: print("Producto no encontrado."); return False