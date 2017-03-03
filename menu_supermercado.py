#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
def menu():
    lista=['a.Compra Producto','b.Ventas Del Dia','c.Inventario','d.Salir']
    datos=json.dumps(lista)
    return datos
def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i