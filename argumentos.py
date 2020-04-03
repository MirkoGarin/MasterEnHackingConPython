#!c:/Python/python.exe
# -*- coding: utf-8 -*-  
def saludo(nombreR, edad):
    print ("Hola {} tienes {}" . format(nombreR,edad))

def main():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    saludo(nombre, edad)

if __name__ == '__main__':
       main()  