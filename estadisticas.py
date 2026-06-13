def pais_mayor_poblacion(paises):
    # Caso de lista vacía
    if not paises:
        return None

    # Asumimos que el primer país es el de mayor población (hipótesis inicial)
    mayor = paises[0]

    # Recorremos el resto de la lista (desde el segundo elemento)
    for pais in paises[1:]:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    return mayor


def pais_menor_poblacion(paises):
    # Caso de lista vacía
    if not paises:
        return None

    # Asumimos que el primer país es el de menor población (hipótesis inicial)
    menor = paises[0]

    # Recorremos el resto de la lista (desde el segundo elemento)
    for pais in paises[1:]:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    return menor


if __name__ == "__main__":
    paises = [
        {"nombre": "Argentina", "poblacion": 45000000, "superficie": 2780400, "continente": "America"},
        {"nombre": "Brasil", "poblacion": 213000000, "superficie": 8515767, "continente": "America"},
        {"nombre": "España", "poblacion": 47000000, "superficie": 505990, "continente": "Europa"},
        {"nombre": "Bulgaria", "poblacion": 6900000, "superficie": 110879, "continente": "Europa"},
    ]

    print("País con mayor población:")
    print(f"  {pais_mayor_poblacion(paises)}")

    print("\nPaís con menor población:")
    print(f"  {pais_menor_poblacion(paises)}")

    # Caso de lista vacía
    print("\nCon lista vacía:")
    print(f"  Mayor: {pais_mayor_poblacion([])}")
    print(f"  Menor: {pais_menor_poblacion([])}")