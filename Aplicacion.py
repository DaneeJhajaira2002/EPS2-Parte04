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
mostrar_producto = """SELECT * FROM Producto where idproducto = ?"""
registrar_producto = """INSERT INTO Producto(codigo,nombre,precio) VALUES (?,?,?)"""
editar_producto = """UPDATE Producto SET codigo=?, nombre=?, precio=? WHERE idproducto=?"""
eliminar_producto = """DELETE FROM Producto WHERE idproducto = ?"""

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
elif(opcion=="2"):
    idproducto = input("Id del producto: ")
    id = int(idproducto)
    cursor.execute(eliminar_producto, (id,))
    conexion.commit()
    print ("\n*** PRODUCTO ELIMINADO CORRECTAMENTE ***")
elif(opcion=="3"):
    idproducto = input("Id del producto: ")
    id = int(idproducto)
    print("*\nDatos actuales del producto***\n")
    cursor.execute(mostrar_producto, (id,))
    producto = cursor.fetchone()
    print("Codigo: " + str(producto[1]))
    print("Nombre: " + producto[2])
    print("Precio: " + str(producto[3]))
    print("\nIngrese los nuevos valores: ")
    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    precio = input("Precio: ")
    cursor.execute(editar_producto, (codigo, nombre, precio, id,))
    conexion.commit()
    print("\n*** PRODUCTO EDITADO EXITOSAMENTE *** ")
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