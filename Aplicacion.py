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

cursor = conexion.cursor()
cursor.execute(tabla_producto)

def menu():
    print("\n\t\Menú Opciones:")
    print("1. Registrar")
    print("2. Eliminar")
    print("3. Editar")
    print("4. Listar")
    print("5. Salir")

menu()