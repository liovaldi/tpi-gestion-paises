# tpi-gestion-paises
# Trabajo Práctico Integrador: Gestión de Datos de Países
## Tecnicatura Universitaria en Programación a Distancia — UTN 
### Materia: Programación 1 : Trabajo practico integrador

## Descripción del Proyecto
Este sistema interactivo en consola permite gestionar de forma eficiente un dataset de países independientes. La aplicación está desarrollada en Python 3.x y procesa información demográfica, geográfica y territorial utilizando estructuras de datos dinámicas y persistencia en archivos locales.

El programa implementa un flujo de control robusto con validaciones estrictas de entrada para evitar fallos de ejecución, garantizando la integridad de los datos almacenados.

## Estructura de los Datos
Cada país se manipula internamente en la memoria del programa como una estructura de diccionario mapeada con las siguientes llaves técnicas:
*`nombre`: Cadena de caracteres (string) que identifica al país.
*`poblacion`: Valor entero (int) que representa la cantidad de habitantes.
* `superficie`: Valor entero (int) con la extensión territorial expresada en km².
*`continente`: Cadena de caracteres (string) que indica la región geográfica.

## Funcionalidades del Sistema
El menú interactivo de la consola expone los siguientes módulos operativos:
1. **Registrar País (Persona A):** Incorpora un nuevo registro al sistema validando la no duplicidad y campos obligatorios.
2.**Modificar Datos (Persona A):** Permite la actualización controlada de los campos de población y superficie de un país existente.
3.**Buscar País (Persona B):** Búsqueda por coincidencia exacta o parcial ignorando mayúsculas y minúsculas.
4.**Filtros Avanzados (Persona B):** Segmentación por continente o rangos cuantitativos de población y superficie.
5.**Ordenamientos Estructurados (Persona B):** Reordenamiento de listas de forma ascendente o descendente bajo múltiples criterios.
6.**Estadísticas Analíticas (Persona B):** Cálculo automático de valores máximos, mínimos, promedios generales e indicadores por continente.

**Reparticion del proyecto:**
**Persona A (Ludmila Iovaldi):** Responsable de la arquitectura base, bucle del menú principal, lógica de lectura/escritura y persistencia de archivos CSV, y desarrollo del módulo ABM (Altas y Modificaciones).  

**Persona B (Gaaston Reynoso):** Responsable de la lógica de consultas complejas, algoritmos de filtrado de datos, criterios de ordenamiento matemático, cálculos estadísticos analíticos y documentación extendida de ejecución.

## Enlaces del Proyecto
*Enlace al Video Demostrativo:*   
*Documentación Académica (PDF):* 