#!/usr/bin/env python3

from bs4 import BeautifulSoup

def mostrar_libro():
    archivo = open("libro.xml", "r")
    texto = archivo.read()

    libro = BeautifulSoup(texto, 'xml') 

    print("\nBOULEVARD")

    titulo = libro.find("titulo")
    if titulo: 
        print("Título: " + titulo.text)
    else:
        print("Título: No disponible")

    autor = libro.find("autor")
    if autor:
        nombre = autor.find("nombre")
        if nombre:
            print("Autor: " + nombre.text) 
        else: 
            print("Autor: No disponible") 

        nacionalidad = autor.find("nacionalidad")
        if nacionalidad: 
            print("Nacionalidad: " + nacionalidad.text)

    else:
        print("Autor: No diponible")

    editorial = libro.find("editorial")
    if editorial: 
        print("Editorial: " + editorial.text)

    publicacion = libro.find("pubilcacion")
    if publicacion: 
        print("Publicación: " + publicacion["year"])

    generos = libro.find_all("genero") 
    if generos: 
        contador = 0
        texto = ""

        while contador < len(generos): 
            texto += generos[contador]["value"] 

            if contador < len(generos) - 1:
                texto += ", "

            contador += 1

        print("Géneros: " + texto)

    else:
        print("Géneros: No disponible")


    idiomas = libro.find_all("idioma")
    if idiomas: 
        contador = 0
        texto = ""

        while contador < len(idiomas):
            texto += idiomas[contador]["value"]

            if contador < len(idiomas) - 1: 
                texto += ", "

            contador += 1

        print("Idiomas: " + texto)

    else:
        print("Idiomas: No disponible")

    saga = libro.find("saga")
    if saga: 
        print("Saga: " + saga["name"])

        volumenes = saga.find_all("volumen")
        contador = 0

        while contador < len(volumenes): 
              vol = volumenes[contador] 
              print(" -Volumen " + vol["num"] + ": " + vol.text)
              contador += 1
    else: 
        print("Saga: No disponible") 

    protagonistas = libro.find_all("protagonista") 
    if protagonistas: 
          contador = 0
          texto = ""

          while contador < len(protagonistas):
              texto += protagonistas[contador]["name"] 

              if contador < len(protagonistas) - 1: 
                texto += ", "

              contador += 1

          print("Protagonistas: " + texto) 

    origen = libro.find("origen")
    if origen: 
        print("Origen: " + origen["value"]) 

    descripcion = libro.find("descripcion")
    if descripcion: 
        print("\nDescripción:\n" + descripcion.text)

mostrar_libro() 
              
























