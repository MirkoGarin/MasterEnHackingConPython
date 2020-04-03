#!c:/Python/python.exe
# -*- coding: utf-8 -*-  
# a = 
archivo = open("archivo2.txt","a")
nombre = input("Nombre: ")
edad = input("Edad: ")
pais = input("Pais: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)
archivo.write("\n")

print("Escribi los datos")

archivo.close()

