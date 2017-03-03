#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Inicio del programa
import menu_supermercado
import menu_producto
import  json
import socket
import os
ruta_s = socket.socket()

#dirección ip del servidor
ruta_s.connect(("localhost", 35000))

while True:

    mensaje = raw_input('>>')
    ruta_s.send(mensaje)
    datos = ruta_s.recv(1024)

    if datos == "bienvenidos":
        print datos
        demenu = menu_supermercado.menu()
        menu_supermercado.menu_lista(demenu)
        opcion = raw_input("digite alguna opcion ")
        ruta_s.send(opcion)
        if opcion == 'a':
            pmenu = menu_producto.menu()
            menu_producto.menu_lista(pmenu)
            #id=raw_input("ingresar id:")
            #cant = raw_input("ingresar cantidad :")
            lista = {'01': 'cafe    10        3500 ', '02': 'azucar   10       2500', '03':
                'arroz    15       3600', '04': 'frijol    15      2600', '05': 'galletas  20      3400'}

            id = raw_input("id producto:")
            cant = raw_input(" cantidad:")
            valor = lista.pop(id)
            print valor






        #if mensaje == 'salir':
         #   break

 #print "Regrese Cuando Quiera"
    # cerrar conexión con el servidor
ruta_s.close()
