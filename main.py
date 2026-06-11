import csv
import os

# --- LOGICA DE PERSISTENCIA (Persona A) ---

def leer_csv(nombre_archivo="paises.csv"):
    """
    Lee el archivo CSV y retorna una lista de diccionarios.
    Maneja errores si el archivo no existe o está corrupto.
    """
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
        print("Error: Archivo no encontrado.")
    except ValueError:
        print("Error: El CSV contiene datos con formatos incorrectos (ej. texto en población).")
    except Exception as e:
        print(f"Ocurrió un error inesperado al leer: {e}")
        
    return lista_paises

def guardar_csv(lista_paises, nombre_archivo="paises.csv"):
    """
    Toma la lista de países que tenemos en Python y la escribe
    adentro del archivo CSV para que los datos queden guardados.
    """
    try:
        with open(nombre_archivo, mode="w", encoding="utf-8", newline="") as archivo:
            # Le decimos cómo se llaman las columnas de nuestro archivo
            campos = ["nombre", "poblacion", "superficie", "continente"]            
            # Creamos el escritor que sabe traducir diccionarios a filas de CSV
            escritor = csv.DictWriter(archivo, fieldnames=campos)            
            # Escribimos los títulos de las columnas (la primera fila)
            escritor.writeheader()            
            # Escribimos todos los países de nuestra lista
            escritor.writerows(lista_paises)            
        print("¡Cambios guardados con éxito en el archivo CSV!")
    except Exception as e:
        print(f"Error al intentar guardar los datos: {e}")

def agregar_pais(lista_paises):
    """
    Pide al usuario los datos de un nuevo país, los valida rigurosamente
    y, si todo es correcto, lo añade a la lista del sistema.
    """
    print("\n--- REGISTRAR NUEVO PAÍS ---")
    
    # 1. Validación del Nombre
    nombre = input("Ingrese el nombre del país: ").strip()
    if not nombre:
        print("Error: El nombre del país no puede quedar vacío.")
        return lista_paises
        
    # Verificamos si el país ya existe en la lista para no duplicarlo
    for pais in lista_paises:
        if pais["nombre"].lower() == nombre.lower():
            print(f"El país '{nombre}' ya se encuentra registrado en el sistema.")
            return lista_paises

    # 2. Validación de la Población (Debe ser un número entero positivo)
    poblacion_input = input("Ingrese la cantidad de población: ").strip()
    if not poblacion_input.isdigit():
        print("Error: La población debe ser un número entero positivo (sin letras ni puntos).")
        return lista_paises
    poblacion = int(poblacion_input)

    # 3. Validación de la Superficie (Debe ser un número entero positivo)
    superficie_input = input("Ingrese la superficie (en km²): ").strip()
    if not superficie_input.isdigit():
        print("Error: La superficie debe ser un número entero positivo.")
        return lista_paises
    superficie = int(superficie_input)

    # 4. Validación del Continente
    continente = input("Ingrese el continente: ").strip()
    if not continente:
        print("Error: El continente no puede quedar vacío.")
        return lista_paises

    # Si pasó todos los filtros, creamos el diccionario del nuevo país
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    # Lo agregamos a la lista que está en la memoria del programa
    lista_paises.append(nuevo_pais)
    print(f"¡{nombre} ha sido agregado exitosamente a la lista local!")
    
    return lista_paises


# --- MENÚ PRINCIPAL Y CONTROLADOR (Persona A) ---

def mostrar_menu():
    print("\n" + "="*30)
    print("      SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*30)
    print("1. Agregar país")
    print("2. Modificar país")
    print("3. Buscar país (Persona B)")
    print("4. Filtrar países (Persona B)")
    print("5. Ordenar países (Persona B)")
    print("6. Ver estadísticas (Persona B)")
    print("7. Salir")
    print("="*30)

def main():
    # Cargamos los datos al iniciar el programa
    archivo_datos = "paises.csv"
    datos_sistema = leer_csv(archivo_datos)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        if opcion == "1":
            # Conectamos las funciones que preparamos
            datos_sistema = agregar_pais(datos_sistema)
            guardar_csv(datos_sistema, archivo_datos)
        elif opcion == "2":
            print("\n[Próximamente] Aquí irá la función modificar_pais()") # Fase 1
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
            print(" Opción inválida. Por favor, elija un número del 1 al 7.")

if __name__ == "__main__":
    main()