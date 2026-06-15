

#MAYOR y MENOR
def pais_mayor_poblacion(paises):
    # lista vacía
    if not paises:
        return None

    # Asumimos que el primer país es el de mayor población luego se compara
    mayor = paises[0]

    # Recorremos el resto de la lista (desde el segundo elemento)
    for pais in paises[1:]:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    return mayor

def pais_menor_poblacion(paises):
    # lista vacía
    if not paises:
        return None

    # Asumimos que el primer país es el de menor población luego comparamos
    menor = paises[0]

    # Recorremos el resto de la lista (desde el segundo elemento)
    for pais in paises[1:]:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    return menor


#PROMEDIOS
def promedio_poblacion(paises):
    # lista vacía
    if not paises:
        return None

    suma = 0
    for pais in paises:
        suma += pais["poblacion"]

    promedio = suma / len(paises)
    return promedio

def promedio_superficie(paises):
    # lista vacía
    if not paises:
        return None

    suma = 0
    for pais in paises:
        suma += pais["superficie"]

    promedio = suma / len(paises)
    return promedio

#CANT CONTINENETES
def cantidad_por_continente(paises):
    resultados = {}

    for pais in paises:
        continente = pais["continente"]

        if continente in resultados:
            resultados[continente] += 1
        else:
            resultados[continente] = 1

    return resultados

if __name__ == "__main__":
    paises = [
        {"nombre": "Argentina", "poblacion": 45000000, "superficie": 2780400, "continente": "America"},
        {"nombre": "Brasil", "poblacion": 213000000, "superficie": 8515767, "continente": "America"},
        {"nombre": "España", "poblacion": 47000000, "superficie": 505990, "continente": "Europa"},
        {"nombre": "Bulgaria", "poblacion": 6900000, "superficie": 110879, "continente": "Europa"},
    ]


    #Prueba funciones MAYOR y MENOR
    print("País con mayor población:")
    print(f"  {pais_mayor_poblacion(paises)}")

    print("\nPaís con menor población:")
    print(f"  {pais_menor_poblacion(paises)}")

    # Caso de lista vacía
    print("\nCon lista vacía:")
    print(f"  Mayor: {pais_mayor_poblacion([])}")
    print(f"  Menor: {pais_menor_poblacion([])}")

    #Prueba funciones PROMEDIO
    print(f"Promedio de población: {promedio_poblacion(paises):.2f}")
    print(f"Promedio de superficie: {promedio_superficie(paises):.2f}")

    # Caso de lista vacía
    print("\nCon lista vacía:")
    print(f"  Promedio población: {promedio_poblacion([])}")
    print(f"  Promedio superficie: {promedio_superficie([])}")

    #Prueba cant continentes
    print(cantidad_por_continente(paises))

    # Caso de lista vacía
    print(cantidad_por_continente([]))