import csv
import os

# --- LOGICA DE PERSISTENCIA ---

def leer_csv(nombre_archivo="paises.csv"): #Lee archivo CSV retorna lista de diccionarios.

    lista_paises = []
    
    # Validación de archivo existente
    if not os.path.exists(nombre_archivo):
        print(f"Alerta: El archivo '{nombre_archivo}' no existe. Se iniciará con una lista vacía.")
        return lista_paises

    try:
        with open(nombre_archivo, mode="r", encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo) # Usa la primera fila como llaves del diccionario
            for fila in lector:
                # Convertimos los datos string a los tipos correspondientes acordados
                pais = {
                    "nombre": fila["nombre"].strip(),
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"].strip()
                }
                lista_paises.append(pais)
    except FileNotFoundError:
        print(" Error: Archivo no encontrado.")
    except ValueError:
        print(" Error: El CSV contiene datos con formatos incorrectos (ej. texto en población).")
    except Exception as e:
        print(f" Ocurrió un error inesperado al leer: {e}")
        
    return lista_paises

def guardar_csv(lista_paises, nombre_archivo="paises.csv"): #Toma lista y pasa a archivo CSV

    try:
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]            
            escritor = csv.DictWriter(archivo, fieldnames=campos)            
            escritor.writeheader()            
            escritor.writerows(lista_paises)            
        print("¡Cambios guardados con éxito en el archivo CSV!")
    except Exception as e:
        print(f"Error al intentar guardar los datos: {e}")

def agregar_pais(lista_paises): #solicitud de datos/validacion

    print("\n--- REGISTRAR NUEVO PAÍS ---")
    
    nombre = input("Ingrese el nombre del país: ").strip()
    if not nombre:
        print("Error: El nombre del país no puede quedar vacío.")
        return lista_paises
        
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"El país '{nombre}' ya se encuentra registrado en el sistema.")
            return lista_paises

    poblacion_input = input("Ingrese la cantidad de población: ").strip()
    if not poblacion_input.isdigit():
        print("Error: La población debe ser un número entero positivo (sin letras ni puntos).")
        return lista_paises
    poblacion = int(poblacion_input)

    superficie_input = input("Ingrese la superficie (en km²): ").strip()
    if not superficie_input.isdigit():
        print("Error: La superficie debe ser un número entero positivo.")
        return lista_paises
    superficie = int(superficie_input)

    continente = input("Ingrese el continente: ").strip()
    if not continente:
        print(" Error: El continente no puede quedar vacío.")
        return lista_paises

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    lista_paises.append(nuevo_pais)
    print(f"¡{nombre} ha sido agregado exitosamente a la lista local!")
    return lista_paises

def modificar_pais(lista_paises):
    """
    Busca un país por nombre y permite al usuario modificar sus campos
    (población, superficie o continente) aplicando las validaciones.
    """
    print("\n--- MODIFICAR DATOS DE UN PAÍS ---")
    nombre_buscar = input("Ingrese el nombre del país que desea modificar: ").strip()
    
    pais_encontrado = None
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre_buscar.lower():
            pais_encontrado = pais
            break
            
    if not pais_encontrado:
        print(f"Error: El país '{nombre_buscar}' no se encuentra registrado.")
        return lista_paises

    print(f"\nPaís seleccionado: {pais_encontrado['nombre']}")
    print(f"1. Modificar Población (Actual: {pais_encontrado['poblacion']})")
    print(f"2. Modificar Superficie (Actual: {pais_encontrado['superficie']})")
    print(f"3. Modificar Continente (Actual: {pais_encontrado['continente']})")
    
    opcion_mod = input("Seleccione qué dato desea modificar (1-3): ").strip()
    
    if opcion_mod == "1":
        nueva_pob = input("Ingrese la nueva cantidad de población: ").strip()
        if not nueva_pob.isdigit() or int(nueva_pob) <= 0:
            print("Error: La población debe ser un número entero positivo.")
            return lista_paises
        pais_encontrado["poblacion"] = int(nueva_pob)
        print(f"¡Población de {pais_encontrado['nombre']} actualizada con éxito!")
        
    elif opcion_mod == "2":
        nueva_sup = input("Ingrese la nueva superficie (en km²): ").strip()
        if not nueva_sup.isdigit() or int(nueva_sup) <= 0:
            print(" Error: La superficie debe ser un número entero positivo.")
            return lista_paises
        pais_encontrado["superficie"] = int(nueva_sup)
        print(f"¡Superficie de {pais_encontrado['nombre']} actualizada con éxito!")
        
    elif opcion_mod == "3":
        nuevo_cont = input("Ingrese el nuevo continente: ").strip()
        if not nuevo_cont:
            print(" Error: El continente no puede quedar vacío.")
            return lista_paises
        pais_encontrado["continente"] = nuevo_cont
        print(f" ¡Continente de {pais_encontrado['nombre']} actualizado con éxito!")
        
    else:
        print("Opción inválida. No se realizaron cambios.")
        
    return lista_paises

# --- MENÚ PRINCIPAL Y CONTROLADOR ---

def mostrar_menu():
    print("\n" + "="*40)
    print("      SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*40)
    print("1. Agregar país")
    print("2. Modificar país")
    print("3. Buscar país (Persona B)")
    print("4. Filtrar países (Persona B)")
    print("5. Ordenar países (Persona B)")
    print("6. Ver estadísticas (Persona B)")
    print("7. Salir")
    print("="*30)

def main():
    archivo_datos = "paises.csv"
    datos_sistema = leer_csv(archivo_datos)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            datos_sistema = agregar_pais(datos_sistema)
            guardar_csv(datos_sistema, archivo_datos)
        elif opcion == "2":
            datos_sistema = modificar_pais(datos_sistema)
            guardar_csv(datos_sistema, archivo_datos)
        elif opcion == "3":
            print("\nOpción no disponible - Módulo a cargo de Persona B.")
        elif opcion == "4":
            print("\nOpción no disponible - Módulo a cargo de Persona B.")
        elif opcion == "5":
            print("\nOpción no disponible - Módulo a cargo de Persona B.")
        elif opcion == "6":
            print("\nOpción no disponible - Módulo a cargo de Persona B.")
        elif opcion == "7":
            print("\n¡Gracias por utilizar el sistema! Saliendo...")
            break
        else:
            print("Opción inválida. Por favor, elija un número del 1 al 7.")

if __name__ == "__main__":
    main()