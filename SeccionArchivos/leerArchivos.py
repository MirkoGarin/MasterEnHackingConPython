#!c:/Python/python.exe
# -*- coding: utf-8 -*-  

#r = read
#w = write 
archivo = open('archivo2.txt','r')
#Muestra los datos desrolijos
#print(archivo.readlines())

#split separa cadenas de texto segun valor pasado
#for l in archivo.read().split('\n'):
   # print(l)
   
#mas prolijos
lista = archivo.read().split('\n')

for n in lista:
    
    print(n)
