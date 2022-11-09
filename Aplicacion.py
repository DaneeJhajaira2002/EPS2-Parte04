# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sqlite3
conexion = sqlite3.connect("BarzolaGonzalesSoto_almacen")

tabla_producto = """CREATE TABLE Producto(
        idproducto INTEGER PRIMARY KEY AUTOINCREMENT,
        codigo NUMBER UNIQUE,
        nombre TEXT,
        precio REAL
        )
        """


listar_productos = """SELECT * FROM PRODUCTO"""
registrar_producto = """INSERT INTO Producto(codigo,nombre,precio) VALUES (?,?,?)"""

cursor = conexion.cursor()
def agregar_espacio(cadena):

    cantidad_espacios = 15 - len(cadena)
    espacios = ""
    for i in range(cantidad_espacios):
        espacios += " "
    return espacios


"""cursor.execute(tabla_producto)"""

def menu():
    print("\n\t Menú Opciones:")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

menu()

opcion = input("\tSeleccione una opcion: ")

if(opcion=="1"):
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    producto = (codigo,nombre,precio)
    cursor.execute(registrar_producto, producto)
    conexion.commit()
    
elif(opcion=="4"):
    cursor.execute(listar_productos)
    productos = cursor.fetchall()
    print("* LISTANDO PRODUCTOS *\n")
    it = 0
    for producto in productos:
       if it == 0:
           print("ID" + agregar_espacio("ID") + "CODIGO" + agregar_espacio("CODIGO")
                 + "NOMBRE" + agregar_espacio("NOMBRE") + "PRECIO")
       print(str(producto[0]) + agregar_espacio(str(producto[0])) + str(producto[1]) 
             + agregar_espacio(str(producto[1])) + (producto[2]) 
             + agregar_espacio(producto[2]) + str(producto[3]))
       it+=1
else:
    print("Gracias... vuelva pronto")
    
    
conexion.close()