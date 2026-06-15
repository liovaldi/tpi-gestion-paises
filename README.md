# Trabajo Práctico Integrador: Gestión de Datos de Países
## Tecnicatura Universitaria en Programación a Distancia — UTN 
### Materia: Programación 1 : Trabajo practico integrador

## Descripción del Proyecto
Este sistema interactivo en consola permite gestionar de forma eficiente un dataset de países independientes. La aplicación está desarrollada en Python 3.x y procesa información demográfica, geográfica y territorial utilizando estructuras de datos dinámicas y persistencia en archivos locales.

El programa implementa un flujo de control robusto con validaciones estrictas de entrada para evitar fallos de ejecución, garantizando la integridad de los datos almacenados.

🎯 Objetivos del Proyecto
Aplicar estructuras de datos (listas y diccionarios).
Utilizar funciones para modularizar el código.
Implementar búsquedas, filtros y ordenamientos.
Gestionar persistencia mediante archivos CSV.
Aplicar validaciones y manejo de errores.
Generar estadísticas sobre conjuntos de datos.

## Estructura de los Datos
Cada país se manipula internamente en la memoria del programa como una estructura de diccionario mapeada con las siguientes llaves técnicas:
*`nombre`: Cadena de caracteres (string) que identifica al país.
*`poblacion`: Valor entero (int) que representa la cantidad de habitantes.
*`superficie`: Valor entero (int) con la extensión territorial expresada en km².
*`continente`: Cadena de caracteres (string) que indica la región geográfica.

⚙️ Funcionalidades
Gestión de países
Agregar países.
Modificar países existentes.
Guardar automáticamente los cambios.
Búsquedas
Buscar países por nombre completo.
Buscar países por coincidencia parcial.
Filtros
Filtrar por continente.
Filtrar por rango de población.
Filtrar por rango de superficie.
Ordenamientos
Ordenar por nombre.
Ordenar por población.
Ordenar por superficie.
Orden ascendente y descendente.
Estadísticas
País con mayor población.
País con menor población.
Promedio de población.
Promedio de superficie.
Cantidad de países por continente.
📂 Estructura del Proyecto
gestion-paises/
│
├── main.py
├── filtros_orden.py
├── estadisticas.py
├── paises.csv
├── README.md
└── informe.pdf
Descripción de los módulos
main.py

Contiene:

Menú principal.
Lectura y escritura del CSV.
Alta de países.
Modificación de países.
Integración de todos los módulos.
filtros_orden.py

Contiene:

Filtros por continente.
Filtros por población.
Filtros por superficie.
Búsquedas por nombre.
Ordenamientos.
estadisticas.py

Contiene:

Cálculo de máximos y mínimos.
Promedios.
Conteo por continente.
paises.csv

Archivo de persistencia utilizado para almacenar los datos del sistema.

🛠️ Requisitos
Python 3.10 o superior.

No requiere librerías externas.

▶️ Ejecución

Clonar el repositorio:

git clone https://github.com/liovaldi/tpi-gestion-paises

Ingresar al directorio:

cd gestion-paises

Ejecutar:

python main.py
📋 Ejemplos de Uso
Ejemplo 1 - Filtrar por continente

Entrada:

Opción: 4
Filtrar por continente
Ingrese continente: Europa

Salida:

España
Francia
Alemania
Italia
Ejemplo 2 - Filtrar por rango de población

Entrada:

Opción: 4
Población mínima: 40000000
Población máxima: 70000000

Salida:

Argentina
España
Francia
Italia
Sudáfrica
Ejemplo 3 - Buscar país

Entrada:

Opción: 3
Buscar: jap

Salida:

Japón
Ejemplo 4 - Ordenar por población (descendente)

Entrada:

Opción: 5
Ordenar por población
Orden descendente

Salida:

India
China
Brasil
Nigeria
Japón
...
Ejemplo 5 - Estadísticas

Entrada:

Opción: 6

Salida:

País con mayor población:
India (1408000000)

País con menor población:
Nueva Zelanda (5000000)

Promedio de población:
280266666.67

Promedio de superficie:
2541625.47

Cantidad por continente:
América: 3
Europa: 4
Asia: 3
África: 3
Oceanía: 2
🧠 Conceptos Aplicados

Durante el desarrollo del proyecto se aplicaron los siguientes conceptos:

Variables y tipos de datos.
Listas.
Diccionarios.
Funciones.
Parámetros y retorno.
Condicionales (if, elif, else).
Bucles (for, while).
Archivos CSV.
Manejo de excepciones.
Algoritmos de búsqueda.
Algoritmos de ordenamiento (Bubble Sort).
Estadística básica.
👥 Integrantes
Gastón Reynoso
Ludmila Iovaldi
🎓 Institución

Tecnicatura Universitaria en Programación

Universidad Tecnológica Nacional (UTN)

📚 Bibliografía
https://docs.python.org/3/
https://docs.python.org/3/library/csv.html
https://greenteapress.com/wp/think-python-2e/
Material de cátedra Programación I - UTN
🔗 Enlaces

Repositorio:
https://github.com/liovaldi/tpi-gestion-paises

Video explicativo:
[Agregar URL]