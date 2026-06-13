#   lista ficticia
def obtener_paises_ficticios():
    return [
        {"nombre": "Argentina", "continente": "América", "poblacion": 46000000, "superficie": 2780400},
        {"nombre": "Canadá", "continente": "América", "poblacion": 38000000, "superficie": 9984670},
        {"nombre": "Japón", "continente": "Asia", "poblacion": 125000000, "superficie": 377975},
        {"nombre": "Egipto", "continente": "África", "poblacion": 110000000, "superficie": 1002450},
        {"nombre": "Francia", "continente": "Europa", "poblacion": 68000000, "superficie": 551695},
        {"nombre": "Australia", "continente": "Oceanía", "poblacion": 26000000, "superficie": 7692024},
        {"nombre": "Sudáfrica", "continente": "África", "poblacion": 60000000, "superficie": 1221037},
        {"nombre": "España", "continente": "Europa", "poblacion": 47000000, "superficie": 505990}
    ]

import unicodedata
#Funcion para sacar tildes y poner en minusculas
def normalizar(texto):
    texto = texto.lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

#programar FILTROS 
def filtrar_por_continente(lista_paises, continente_buscado):
    #  lógica 
    # Crear una lista vacía para los resultados
    resultados = []
    
    # Recorrer cada país de la lista con un bucle
    for pais in lista_paises:
        # Comparar convirtiendo ambos strings a minúsculas (.lower())
        if normalizar(pais["continente"]) == normalizar(continente_buscado):
            # Si coinciden, agregar el país a los resultados
            resultados.append(pais)
            
    # Retornar la lista de resultados
    return resultados


def filtrar_por_rango_poblacion(paises, minimo, maximo):
    # Validar que ambos valores sean números positivos
    if minimo < 0 or maximo < 0:
        return None

    # Validar que el mínimo no sea mayor que el máximo
    if minimo > maximo:
        return None

    resultados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            resultados.append(pais)

    return resultados


def filtrar_por_rango_superficie(paises, minimo, maximo):
    # Ambos valores sean números positivos
    if minimo < 0 or maximo < 0:
        return None

    # Mínimo no sea mayor que el máximo
    if minimo > maximo:
        return None

    resultados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            resultados.append(pais)

    return resultados

#Buscar PAIS
def buscar_pais(paises, texto):
    resultados = []
    texto_normalizado = normalizar(texto)

    for pais in paises:
        nombre_normalizado = normalizar(pais["nombre"])

        # Verificamos si el texto buscado está contenido en el nombre
        if texto_normalizado in nombre_normalizado:
            resultados.append(pais)

    return resultados




#programar ORDENAMIENTOS
#por NOMBRE
def ordenar_por_nombre(paises, ascendente=True):
    # Copiamos la lista para no modificar la original
    lista = paises.copy()
    n = len(lista)
#BUBLE SORT: recorrer la lista comparando elementos de a pares consecutivos, y si están en el orden incorrecto, intercambiarlos
    for i in range(n):
        for j in range(0, n - i - 1):
            if ascendente:
                # Si el actual es mayor que el siguiente, intercambiamos
                if lista[j]["nombre"] > lista[j + 1]["nombre"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                # Para descendente, intercambiamos cuando el actual es menor
                if lista[j]["nombre"] < lista[j + 1]["nombre"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

#por POBLACION
def ordenar_por_poblacion(paises, ascendente=True):
    lista = paises.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ascendente:
                if lista[j]["poblacion"] > lista[j + 1]["poblacion"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j]["poblacion"] < lista[j + 1]["poblacion"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

#por SUPERFICIE
def ordenar_por_superficie(paises, ascendente=True):
    lista = paises.copy()
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i - 1):
            if ascendente:
                if lista[j]["superficie"] > lista[j + 1]["superficie"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                if lista[j]["superficie"] < lista[j + 1]["superficie"]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


#import os #Te da herramientas para interactuar con el sistema operativo de tu computadora
#import csv #Importa el módulo nativo de Python especializado en archivos csv
from main import leer_csv  # importamos la función desde main.py

# bloque de pruebas
if __name__ == "__main__":
    
    
    # (En el futuro, acá llamar a la función que lee el CSV real)
    # paises = leer_csv_real() 
    paises = leer_csv("paises.csv")

    # Chequeo rápido para confirmar que se leyó bien
    print(f"Cantidad de países leídos: {len(paises)}")
    if not paises:
        print("La lista está vacía (no se encontró el CSV o está vacío). No se pueden correr las pruebas.")
    else:
        print(f"Ejemplo: {paises[0]}\n")






    # Usamos los datos ficticios
    #paises = obtener_paises_ficticios()
    

    print("-------------FILTRADO POR CONTINENTE--------------------/n")

    print("Buscando 'america':")
    for p in filtrar_por_continente(paises, "america"):
        print(f"  - {p['nombre']}")

    print("\nBuscando 'EUROPA':")
    for p in filtrar_por_continente(paises, "EUROPA"):
        print(f"  - {p['nombre']}")

    print("\nBuscando 'África':")
    for p in filtrar_por_continente(paises, "África"):
        print(f"  - {p['nombre']}")

    print("\nBuscando 'Oceanía':")
    resultado = filtrar_por_continente(paises, "Oceanía")
    if not resultado:
        print("  No se encontraron países.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']}")

    
    print("-------------FILTRADO POR RANGO POBLACION--------------------/n")
    # Caso 1: rango válido con resultados
    print("Población entre 40 y 70 millones:")
    resultado = filtrar_por_rango_poblacion(paises, 40000000, 70000000)
    if resultado is None:
        print("  Rango inválido.")
    elif not resultado:
        print("  No hay países en ese rango.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']} ({p['poblacion']})")

    # Caso 2: rango válido pero sin ningún país que entre
    print("\nPoblación entre 1 y 1000 (no entra nadie):")
    resultado = filtrar_por_rango_poblacion(paises, 1, 1000000000)
    if resultado is None:
        print("  Rango inválido.")
    elif not resultado:
        print("  No hay países en ese rango.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']} ({p['poblacion']})")

    # Caso 3: mínimo mayor que máximo
    print("\nMínimo mayor que máximo (100 millones - 10 millones):")
    resultado = filtrar_por_rango_poblacion(paises, 100000000, 10000000)
    if resultado is None:
        print("  Error: el mínimo no puede ser mayor que el máximo.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']} ({p['poblacion']})")

    # Caso 4: valores negativos
    print("\nValores negativos (-5 a 100):")
    resultado = filtrar_por_rango_poblacion(paises, -5, 100)
    if resultado is None:
        print("  Error: los valores deben ser números positivos.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']} ({p['poblacion']})")


    print("-------------FILTRADO POR SUPERFICIE--------------------/n")

    # Caso 1: rango válido con resultados
    print("Superficie entre 300000 y 700000 km²:")
    resultado = filtrar_por_rango_superficie(paises, 300000, 700000)
    if resultado is None:
        print("  Rango inválido.")
    elif not resultado:
        print("  No hay países en ese rango.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']} ({p['superficie']} km²)")

    # Caso 2: rango válido pero sin ningún país que entre
    print("\nSuperficie entre 1 y 1000 km² (no entra nadie):")
    resultado = filtrar_por_rango_superficie(paises, 1, 1000)
    if resultado is None:
        print("  Rango inválido.")
    elif not resultado:
        print("  No hay países en ese rango.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']} ({p['superficie']} km²)")

    # Caso 3: mínimo mayor que máximo
    print("\nMínimo mayor que máximo (8000000 - 500000):")
    resultado = filtrar_por_rango_superficie(paises, 8000000, 500000)
    if resultado is None:
        print("  Error: el mínimo no puede ser mayor que el máximo.")
    else:
        for p in resultado:
            print(f"  - {p['nombre']} ({p['superficie']} km²)")


    print("----------------ORDENAMIENTOS-------------------/n")

    def mostrar(lista, titulo):
        print(f"\n{titulo}")
        for p in lista:
            print(f" -{p['nombre']} | pob: {p['poblacion']} | sup: {p['superficie']}")

    mostrar(paises, "Lista original:")

    # Ordenar por nombre
    mostrar(ordenar_por_nombre(paises, ascendente=True), "Por nombre (ascendente):")
    mostrar(ordenar_por_nombre(paises, ascendente=False), "Por nombre (descendente):")

    # Ordenar por población
    mostrar(ordenar_por_poblacion(paises, ascendente=True), "Por población (ascendente):")
    mostrar(ordenar_por_poblacion(paises, ascendente=False), "Por población (descendente):")

    # Ordenar por superficie
    mostrar(ordenar_por_superficie(paises, ascendente=True), "Por superficie (ascendente):")
    mostrar(ordenar_por_superficie(paises, ascendente=False), "Por superficie (descendente):")

    # Verificamos que la lista original no haya sido modificada
    mostrar(paises, "Lista original (después de ordenar, debe seguir igual):")



    print("----------------BÚSQUEDA POR NOMBRE-------------------/n")
    def mostrar_resultado(texto):
        print(f"\nBuscando '{texto}':")
        resultado = buscar_pais(paises, texto)
        if not resultado:
            print("  No se encontraron países.")
        else:
            for p in resultado:
                print(f"  - {p['nombre']}")

    # Caso 1: coincidencia parcial que matchea varios países
    mostrar_resultado("ar")          
    # Caso 2: mayúsculas/minúsculas mezcladas
    mostrar_resultado("JaPON")      
    # Caso 3: con tilde, buscando sin tilde
    mostrar_resultado("sudáfrica")     
    # Caso 4: sin coincidencias
    mostrar_resultado("xyz")         