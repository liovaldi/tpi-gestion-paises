import csv
import os

# --- LOGICA DE PERSISTENCIA ---

def leer_csv(nombre_archivo="paises.csv"):
    """
    Lee el archivo CSV y retorna una lista de diccionarios.
    Maneja errores si el archivo no existe o está corrupto.
    """
    lista_paises = []
    
    # Validación de archivo existente
    if not os.path.exists(nombre_archivo):
        print(f" Alerta: El archivo '{nombre_archivo}' no existe. Se iniciará con una lista vacía.")
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
            print("\n[Próximamente] Aquí irá la función agregar_pais()") # Fase 1
        elif opcion == "2":
            print("\n[Próximamente] Aquí irá la función modificar_pais()") # Fase 1
        elif opcion == "3":
            print("\nOpción no disponible - Módulo a cargo de Persona B.") # Marcador de posición
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
            print("❌ Opción inválida. Por favor, elija un número del 1 al 7.")

if __name__ == "__main__":
    main()