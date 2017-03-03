#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
def menu():
    lista=['id  nombre  cantidad  precio ','01    cafe    10        3500 ' ,'02  azucar   10       2500','03   arroz    15       3600','04  frijol    15      2600','05  galletas  20      3400']
    datos=json.dumps(lista)
    return datos

def menu_lista(cadena):
    lista=json.loads(cadena)
    for i in lista:
        print i

def diccionario():
    lista = {'01': 'cafe    10        3500 ', '02': 'azucar   10       2500', '03':
        'arroz    15       3600', '04': 'frijol    15      2600', '05': 'galletas  20      3400'}

    id = raw_input("id producto:")
    cant = raw_input("id cantidad:")
    valor = lista.pop(id)
    return valor
def menup_lista(cadena):
    listap=json.loads(cadena)
    for i in listap:
        print i