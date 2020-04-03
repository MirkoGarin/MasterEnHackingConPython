#!c:/Python/python.exe
# -*- coding: utf-8 -*-  
#w = write

archivo = open("archivo2.txt","w")
nombre = input("Nombre: ")
edad = input("Edad: ")
pais = input("Pais: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)
archivo.write("\n")
archivo.write(pais)
archivo.write("\n")

print("Escribi siguientes datos los datos")

archivo.close()