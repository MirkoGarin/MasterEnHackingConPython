#!c:/Python/python.exe
# -*- coding: utf-8 -*-  
def saludo(nombre1, edad1):
    print ("Hola {} tienes {}" . format(nombre1,edad1))

def main():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    saludo(nombre, edad)

if __name__ == '__main__':
       main()  