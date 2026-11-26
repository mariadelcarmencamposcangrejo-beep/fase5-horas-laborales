"""Fase 5 - Problema 5: horas laborales. Ejemplo para revisar y sustentar."""

# Cada fila contiene: nombre, lunes, martes, miércoles, jueves y viernes.
HORAS_TRABAJADAS = [
    ["Ana", 8, 8, 8, 8, 8],
    ["Luis", 9, 9, 9, 9, 9],
    ["Diana", 7, 8, 8, 7, 8],
    ["Carlos", 8, 8, 8, 8, 9.5],
]


def analizar_jornada(horas):
    """Devuelve el total de horas y la clasificación de la jornada."""
    total = 0
    for horas_dia in horas:
        total += horas_dia

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario estándar"

    return total, clasificacion


def mostrar_informe(matriz):
    """Muestra las horas y la clasificación de los cuatro trabajadores."""
    print("INFORME DE HORAS LABORALES")
    print("-" * 56)
    print(f"{'Trabajador':<15}{'Horas semanales':<20}Clasificación")
    print("-" * 56)

    for trabajador in matriz:
        nombre = trabajador[0]
        horas = trabajador[1:]
        total, clasificacion = analizar_jornada(horas)
        print(f"{nombre:<15}{total:<20g}{clasificacion}")


if __name__ == "__main__":
    mostrar_informe(HORAS_TRABAJADAS)
