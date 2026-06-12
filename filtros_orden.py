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

#programar filtros 
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


# bloque de pruebas
if __name__ == "__main__":
    
    
    # (En el futuro, acá llamar a la función que lee el CSV real)
    # paises = leer_csv_real() 

    # Usamos los datos ficticios
    paises = obtener_paises_ficticios()
    
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

    

