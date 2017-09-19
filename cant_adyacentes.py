def life_crear(mapa):
    """
    Crea el estado inicial de Game of life a partir de una disposición
    representada con los caracteres '.' y '#'.

    `mapa` debe ser una lista de cadenas, donde cada cadena representa una
    fila del tablero, y cada caracter puede ser '.' (vacío) o '#' (célula).
    Todas las filas deben tener la misma cantidad decaracteres.

    Devuelve el estado del juego, que es una lista de listas donde cada
    sublista representa una fila, y cada elemento de la fila es False (vacío)
    o True (célula).
    """
    mapa_true_false = []
    for fila in mapa:
        sublista_temporal = []
        for elemento in fila:
            if elemento == '#':
                sublista_temporal.extend([True])
            else:
                sublista_temporal.extend([False])
        mapa_true_false.append(sublista_temporal)
    return mapa_true_false













def cant_adyacentes(life, f, c):
    """
    Calcula la cantidad de células adyacentes a la celda en la fila `f` y la
    columna `c`.

    Importante: El "tablero" se considera "infinito": las celdas del borde
    izquierdo están conectadas a la izquierda con las celdas del borde
    derecho, y viceversa. Las celdas del borde superior están conectadas hacia
    arriba con las celdas del borde inferior, y viceversa.
    """
    cant_filas = len(life)
    cant_columnas = len(life[0])
    celdas_totales = [life[(f+i)%cant_filas][(c+j)%cant_columnas] for i in range(-1,2) for j in range(-1,2) if not ( j == 0 and i == 0)]
    print(celdas_totales)

    numero_vivas = 0
    for celda in celdas_totales:
        if celda:
            numero_vivas += 1
    return numero_vivas



def pruebas_cant_adyacentes():
    """Prueba el correcto funcionamiento de cant_adyacentes()."""
    assert cant_adyacentes(life_crear(['.']), 0, 0) == 0
    assert cant_adyacentes(life_crear(['..', '..']), 0, 0) == 0
    assert cant_adyacentes(life_crear(['..', '..']), 0, 1) == 0
    assert cant_adyacentes(life_crear(['##', '..']), 0, 0) == 2
    assert cant_adyacentes(life_crear(['##', '..']), 0, 1) == 2
    assert cant_adyacentes(life_crear(['#.', '.#']), 0, 0) == 4
    assert cant_adyacentes(life_crear(['##', '##']), 0, 0) == 8
    assert cant_adyacentes(life_crear(['.#.', '#.#', '.#.']), 1, 1) == 4
    assert cant_adyacentes(life_crear(['.#.', '..#', '.#.']), 1, 1) == 3

pruebas_cant_adyacentes()
print(cant_adyacentes(life_crear([
        '........#.',
        '........#.',
        '........#.',
        '...##.....',
        '...##.....',
        '.....##...',
        '.....##...',
        '..........',
    ]),1,9))