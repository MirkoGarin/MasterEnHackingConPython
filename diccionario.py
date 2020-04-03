#!c:/Python/python.exe
# -*- coding: utf-8 -*-

diccionario = dict(nombre="mirko",plataforma="udemy", edad="41")
#print(diccionario["nombre"])
#diccionario vacio
#diccio = {}

#Items
#a = diccionario.items()
#print (a)

#copy
#b = diccionario.copy()
#print(b)

#keys
#keys = diccionario.keys()
#print(keys)

#Values
#values = diccionario.values()
#print(values)

#Con Bucle For
for n in diccionario.keys():
    print(" {} Su valor es: {} " . format(n,diccionario[n]))