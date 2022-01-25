import sudoku
import traceback

# Si las pruebas se ven mal en tu terminal, probá cambiando el valor
# de esta constante a True para desactivar los colores ANSI.
TERMINAL_SIN_COLOR = False

REGIONES = (
    ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)),
    ((0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)),
    ((0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)),

    ((3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)),
    ((3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)),
    ((3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)),
    
    ((6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)),
    ((6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)),
    ((6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)),
)

def _obtener_sudoku_enunciado():
    '''
    Devuelve un juego de sudoku creado con la representación que está en la
    documentación de sudoku.crear_juego. 
    
    Para simplificar, en las pruebas se referirá a este sudoku como
    SUDOKU_ENUNCIADO.
    '''

    return [
        [0, 0, 3,  0, 2, 0,  6, 0, 0],
        [9, 0, 0,  3, 0, 5,  0, 0, 1],
        [0, 0, 1,  8, 0, 6,  4, 0, 0],
        [0, 0, 8,  1, 0, 2,  9, 0, 0],
        [7, 0, 0,  0, 0, 0,  0, 0, 8],
        [0, 0, 6,  7, 0, 8,  2, 0, 0],
        [0, 0, 2,  6, 0, 9,  5, 0, 0],
        [8, 0, 0,  2, 0, 3,  0, 0, 9],
        [0, 0, 5,  0, 1, 0,  3, 0, 0],
    ]

def test_crear_juego_representacion_enunciado():
    juego = sudoku.crear_juego('\n'.join([
        "003020600",
        "900305001",
        "001806400",
        "008102900",
        "700000008",
        "006708200",
        "002609500",
        "800203009",
        "005010300",
    ]))
    assert juego == [
        [0, 0, 3,  0, 2, 0,  6, 0, 0],
        [9, 0, 0,  3, 0, 5,  0, 0, 1],
        [0, 0, 1,  8, 0, 6,  4, 0, 0],
        [0, 0, 8,  1, 0, 2,  9, 0, 0],
        [7, 0, 0,  0, 0, 0,  0, 0, 8],
        [0, 0, 6,  7, 0, 8,  2, 0, 0],
        [0, 0, 2,  6, 0, 9,  5, 0, 0],
        [8, 0, 0,  2, 0, 3,  0, 0, 9],
        [0, 0, 5,  0, 1, 0,  3, 0, 0],
    ], f'El estado de juego obtenido para SUDOKU_ENUNCIADO es incorrecto.'

def test_crear_juego_todos_cero():
    juego = sudoku.crear_juego('\n'.join([
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
        "000000000",
    ]))
    assert juego == [
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
    ], f'El estado de juego obtenido es incorrecto para un sudoku vacío.'

def test_hay_valor_en_fila_devuelve_verdadero():
    juego = _obtener_sudoku_enunciado()

    VALORES_EN_FILAS = (
        (3, 2, 6),
        (9, 3, 5, 1),
        (1, 8, 6, 4),
        (8, 1, 2, 9),
        (7, 8),
        (6, 7, 8, 2),
        (2, 6, 9, 5),
        (8, 2, 3, 9),
        (5, 1, 3),
    )

    for fila, valores in enumerate(VALORES_EN_FILAS):
        for valor in valores:
            assert sudoku.hay_valor_en_fila(juego, fila, valor), \
                f'hay_valor_en_fila(SUDOKU_ENUNCIADO, {fila}, {valor}) devolvió Falso.'
    
    assert juego == _obtener_sudoku_enunciado(), \
        f'hay_valor_en_fila modificó el juego'

def test_hay_valor_en_fila_devuelve_falso():
    juego = _obtener_sudoku_enunciado()

    VALORES_FALTANTES_EN_FILAS = (
        (1, 4, 5, 7, 8, 9),
        (2, 4, 6, 7, 8),
        (2, 3, 5, 7, 9),
        (3, 4, 5, 6, 7),
        (1, 2, 3, 4, 5, 6, 9),
        (1, 3, 4, 5, 9),
        (1, 3, 4, 7, 8),
        (1, 4, 5, 6, 7),
        (2, 4, 6, 7, 8, 9),
    )

    for fila, valores in enumerate(VALORES_FALTANTES_EN_FILAS):
        for valor in valores:
            assert not sudoku.hay_valor_en_fila(juego, fila, valor), \
                f'hay_valor_en_fila(SUDOKU_ENUNCIADO, {fila}, {valor}) devolvió Verdadero.'

    assert juego == _obtener_sudoku_enunciado(), \
        f'hay_valor_en_fila modificó el juego'

def test_hay_valor_en_columna_devuelve_verdadero():
    juego = _obtener_sudoku_enunciado()

    VALORES_EN_COLUMNAS = (
        (9, 7, 8),
        tuple(),
        (3, 1, 8, 6, 2, 5),
        (3, 8, 1, 7, 6, 2),
        (2, 1),
        (5, 6, 2, 8, 9, 3),
        (6, 4, 9, 2, 5, 3),
        tuple(),
        (1, 8, 9),
    )

    for columna, valores in enumerate(VALORES_EN_COLUMNAS):
        for valor in valores:
            assert sudoku.hay_valor_en_columna(juego, columna, valor), \
                f'hay_valor_en_columna(SUDOKU_ENUNCIADO, {columna}, {valor}) devolvió Falso.'
    
    assert juego == _obtener_sudoku_enunciado(), \
        f'hay_valor_en_columna modificó el juego'

def test_hay_valor_en_columna_devuelve_falso():
    juego = _obtener_sudoku_enunciado()

    VALORES_FALTANTES_EN_COLUMNAS = (
        (1, 2, 3, 4, 5, 6),
        (1, 2, 3, 4, 5, 6, 7, 8, 9),
        (4, 7, 9),
        (4, 5, 9),
        (3, 4, 5, 6, 7, 8, 9),
        (1, 4, 7),
        (1, 7, 8),
        (1, 2, 3, 4, 5, 6, 7, 8, 9),
        (2, 3, 4, 5, 6, 7)
    )

    for columna, valores in enumerate(VALORES_FALTANTES_EN_COLUMNAS):
        for valor in valores:
            assert not sudoku.hay_valor_en_columna(juego, columna, valor), \
                f'hay_valor_en_columna(SUDOKU_ENUNCIADO, {columna}, {valor}) devolvió Verdadero.'
    
    assert juego == _obtener_sudoku_enunciado(), \
        f'hay_valor_en_columna modificó el juego'

def test_obtener_origen_region():
    ESQUINAS_CUADRANTES = (
        (0, 0), (0, 3), (0, 6),
        (3, 0), (3, 3), (3, 6),
        (6, 0), (6, 3), (6, 6),
    )

    for esquina_esperada, celdas in zip(ESQUINAS_CUADRANTES, REGIONES):
        for f, c in celdas:
            esquina = sudoku.obtener_origen_region(f, c)
            assert esquina == esquina_esperada, \
                f'obtener_region_celda({f}, {c}) dió {esquina} != {esquina_esperada}'

def test_hay_valor_en_region_devuelve_verdadero():
    juego = _obtener_sudoku_enunciado()

    VALORES_EN_REGION = (
        (3, 9, 1), (2, 3, 5, 8, 6), (6, 1, 4),
        (8, 7, 6), (1, 2, 7, 8),    (9, 8, 2),
        (2, 8, 5), (6, 9, 2, 3, 1), (5, 9, 3)
    )

    for region, valores in zip(REGIONES, VALORES_EN_REGION):
        # Revisar que para todos los valores que hay en esa región...
        for valor in valores:
            # ...en todas las posiciones de esa región...
            for fila, columna in region:
                # ...devuelva Verdadero
                assert sudoku.hay_valor_en_region(juego, fila, columna, valor), \
                    f'hay_valor_en_region(SUDOKU_ENUNCIADO, {fila}, {columna}, {valor}) devolvió Falso.'
    
    assert juego == _obtener_sudoku_enunciado(), \
        f'hay_valor_en_region modificó el juego'

def test_hay_valor_en_region_devuelve_falso():
    juego = _obtener_sudoku_enunciado()

    VALORES_FALTANTES_EN_REGION = (
        (2, 4, 5, 6, 7, 8), (1, 4, 7, 9),    (2, 3, 5, 7, 8, 9),
        (1, 2, 3, 4, 5, 9), (3, 4, 5, 6, 9), (1, 3, 4, 5, 6, 7),
        (1, 3, 4, 6, 7, 9), (4, 5, 7, 8),    (1, 2, 4, 6, 7, 8)
    )

    for region, valores in zip(REGIONES, VALORES_FALTANTES_EN_REGION):
        # Revisar que para todos los valores que no están en esa región...
        for valor in valores:
            # ...en todas las posiciones de esa región...
            for fila, columna in region:
                # ...devuelva Falso
                assert not sudoku.hay_valor_en_region(juego, fila, columna, valor), \
                    f'hay_valor_en_region(SUDOKU_ENUNCIADO, {fila}, {columna}, {valor}) devolvió Verdadero.'

    assert juego == _obtener_sudoku_enunciado(), \
        f'hay_valor_en_region modificó el juego'

def test_es_movimiento_valido_vacio_es_invalido():
    juego = _obtener_sudoku_enunciado()

    for fila in range(sudoku.ALTO_TABLERO):
        for columna in range(sudoku.ANCHO_TABLERO):
            assert not sudoku.es_movimiento_valido(juego, fila, columna, sudoku.VACIO), \
                f'es_movimiento_valido(SUDOKU_ENUNCIADO, {fila}, {columna}, VACIO) devolvió Verdadero'

    assert juego == _obtener_sudoku_enunciado(), \
        f'es_movimiento_valido modificó el juego'

def test_es_movimiento_valido_solucion_son_validos():
    juego = _obtener_sudoku_enunciado()

    SUDOKU_RESOLUCION = [
        [4, 8, 0,  9, 0, 1,  0, 5, 7],
        [0, 6, 7,  0, 4, 0,  8, 2, 0],
        [2, 5, 0,  0, 7, 0,  0, 9, 3],
        [5, 4, 0,  0, 3, 0,  0, 7, 6],
        [0, 2, 9,  5, 6, 4,  1, 3, 0],
        [1, 3, 0,  0, 9, 0,  0, 4, 5],
        [3, 7, 0,  0, 8, 0,  0, 1, 4],
        [0, 1, 4,  0, 5, 0,  7, 6, 0],
        [6, 9, 0,  4, 0, 7,  0, 8, 2]
    ]

    for f, fila in enumerate(SUDOKU_RESOLUCION):
        for c, valor in enumerate(fila):
            if valor == 0:
                continue
            
            assert sudoku.es_movimiento_valido(juego, f, c, valor), \
                f'es_movimiento_valido(SUDOKU_ENUNCIADO, {f}, {c}, {valor}) devolvió Falso.'
    
    assert juego == _obtener_sudoku_enunciado(), \
        f'es_movimiento_valido modificó el juego'

def test_es_movimiento_valido_enunciado_son_invalidos():
    juego = _obtener_sudoku_enunciado()
    SUDOKU_ENUNCIADO = _obtener_sudoku_enunciado()

    for f, fila in enumerate(SUDOKU_ENUNCIADO):
        for c, valor in enumerate(fila):
            if valor == 0:
                continue
            
            assert not sudoku.es_movimiento_valido(juego, f, c, valor), \
                f'es_movimiento_valido(SUDOKU_ENUNCIADO, {f}, {c}, {valor}) devolvió Verdadero.'

    assert juego == _obtener_sudoku_enunciado(), \
        f'es_movimiento_valido modificó el juego'

def test_insertar_valor_valido():
    juego = _obtener_sudoku_enunciado()
    
    estado_esperado = _obtener_sudoku_enunciado()
    estado_esperado[0][0] = 4

    modificado = sudoku.insertar_valor(juego, 0, 0, 4)
    assert modificado == estado_esperado, \
        f'insertar_valor(SUDOKU_ENUNCIADO, 0, 0, 4) no devolvió el estado esperado'
    
    assert juego == _obtener_sudoku_enunciado(), \
        f'insertar_valor(SUDOKU_ENUNCIADO, 0, 0, 4) modificó el estado original'

def test_insertar_valor_solucion_completa():
    juego = _obtener_sudoku_enunciado()

    SUDOKU_RESOLUCION = [
        [4, 8, 0,  9, 0, 1,  0, 5, 7],
        [0, 6, 7,  0, 4, 0,  8, 2, 0],
        [2, 5, 0,  0, 7, 0,  0, 9, 3],
        [5, 4, 0,  0, 3, 0,  0, 7, 6],
        [0, 2, 9,  5, 6, 4,  1, 3, 0],
        [1, 3, 0,  0, 9, 0,  0, 4, 5],
        [3, 7, 0,  0, 8, 0,  0, 1, 4],
        [0, 1, 4,  0, 5, 0,  7, 6, 0],
        [6, 9, 0,  4, 0, 7,  0, 8, 2]
    ]

    for f, fila in enumerate(SUDOKU_RESOLUCION):
        for c, valor in enumerate(fila):
            if valor == 0:
                continue
            
            modificado = sudoku.insertar_valor(juego, f, c, valor)

            assert modificado[f][c] == SUDOKU_RESOLUCION[f][c], \
                f'insertar_valor(SUDOKU_ENUNCIADO, {f}, {c}, {valor}) no insertó el valor ({modificado[f][c]} != {valor})'

            assert modificado != juego, \
                f'insertar_valor(SUDOKU_ENUNCIADO, {f}, {c}, {valor}) modificó el estado pasado por parámetro'

            juego = modificado

def test_insertar_valor_enunciado_devuelve_mismo_estado():
    juego = _obtener_sudoku_enunciado()

    SUDOKU_ENUNCIADO = _obtener_sudoku_enunciado()

    for f, fila in enumerate(SUDOKU_ENUNCIADO):
        for c, valor in enumerate(fila):
            if valor == 0:
                continue
            
            modificado = sudoku.insertar_valor(juego, f, c, valor)

            assert modificado[f][c] == SUDOKU_ENUNCIADO[f][c], \
                f'insertar_valor(SUDOKU_ENUNCIADO, {f}, {c}, {valor}) modificó el juego'

            assert juego == SUDOKU_ENUNCIADO, \
                f'insertar_valor(SUDOKU_ENUNCIADO, {f}, {c}, {valor}) modificó el estado pasado por parámetro'


def test_insertar_valor_invalido_devuelve_mismo_estado():
    juego = _obtener_sudoku_enunciado()
    
    estado_esperado = _obtener_sudoku_enunciado()

    modificado = sudoku.insertar_valor(juego, 1, 0, 9)
    assert modificado == estado_esperado, \
        'insertar_valor(SUDOKU_ENUNCIADO, 1, 0, 9) no devolvió el estado esperado'
    
    assert juego == _obtener_sudoku_enunciado(), \
        'insertar_valor(SUDOKU_ENUNCIADO, 1, 0, 9) modificó el estado original'
    
def test_borrar_valor():
    juego = _obtener_sudoku_enunciado()
    
    for f in range(sudoku.ALTO_TABLERO):
        for c in range(sudoku.ANCHO_TABLERO):
            modificado = sudoku.borrar_valor(juego, f, c)
            
            if juego[f][c] == 0:
                assert modificado[f][c] == 0, \
                    f'borrar_valor(SUDOKU_ENUNCIADO, {f}, {c}) devolvió un estado incorrecto'
                
                assert modificado == juego, \
                    f'borrar_valor(SUDOKU_ENUNCIADO, {f}, {c}) modificó el estado pasado por parámetro'
            else:
                modificado = sudoku.borrar_valor(juego, f, c)
                assert modificado[f][c] == 0, \
                    f'borrar_valor(SUDOKU_ENUNCIADO, {f}, {c}) no borró el valor'
                
                assert juego != modificado, \
                    f'borrar_valor(SUDOKU_ENUNCIADO, {f}, {c}) modificó el estado pasado por parámetro'
                
                juego = modificado

def test_esta_terminado_sin_resolver():
    juego = _obtener_sudoku_enunciado()
    assert not sudoku.esta_terminado(juego), \
        f'esta_terminado(SUDOKU_ENUNCIADO) devolvió Verdadero'
    assert juego == _obtener_sudoku_enunciado(), \
        f'esta_terminado modificó el juego pasado por parámetro'

def test_esta_terminado_resuelto():
    juego = [
        [4, 8, 3, 9, 2, 1, 6, 5, 7],
        [9, 6, 7, 3, 4, 5, 8, 2, 1],
        [2, 5, 1, 8, 7, 6, 4, 9, 3],
        [5, 4, 8, 1, 3, 2, 9, 7, 6],
        [7, 2, 9, 5, 6, 4, 1, 3, 8],
        [1, 3, 6, 7, 9, 8, 2, 4, 5],
        [3, 7, 2, 6, 8, 9, 5, 1, 4],
        [8, 1, 4, 2, 5, 3, 7, 6, 9],
        [6, 9, 5, 4, 1, 7, 3, 8, 2]
    ]
    assert sudoku.esta_terminado(juego), \
        f'esta_terminado(SUDOKU_ENUNCIADO_RESUELTO) devolvió Falso'
    
    SUDOKU_RESUELTO = [
        [4, 8, 3, 9, 2, 1, 6, 5, 7],
        [9, 6, 7, 3, 4, 5, 8, 2, 1],
        [2, 5, 1, 8, 7, 6, 4, 9, 3],
        [5, 4, 8, 1, 3, 2, 9, 7, 6],
        [7, 2, 9, 5, 6, 4, 1, 3, 8],
        [1, 3, 6, 7, 9, 8, 2, 4, 5],
        [3, 7, 2, 6, 8, 9, 5, 1, 4],
        [8, 1, 4, 2, 5, 3, 7, 6, 9],
        [6, 9, 5, 4, 1, 7, 3, 8, 2]
    ]

    assert juego == SUDOKU_RESUELTO, f'esta_terminado modificó el juego pasado por parámetro'

def test_obtener_valor():
    juego = _obtener_sudoku_enunciado()
    SUDOKU_ENUNCIADO = _obtener_sudoku_enunciado()

    for f, fila in enumerate(SUDOKU_ENUNCIADO):
        for c, valor in enumerate(fila):
            if valor == 0:
                continue
            
            obtenido = sudoku.obtener_valor(juego, f, c)
            assert SUDOKU_ENUNCIADO[f][c] == obtenido, \
                f'obtener_valor(SUDOKU_ENUNCIADO, {f}, {c}) = {obtenido} != {SUDOKU_ENUNCIADO[f][c]}'
            
            assert juego == SUDOKU_ENUNCIADO, \
                f'obtener_valor modificó el estado recibido por parámetro'

def test_hay_movimientos_posibles_vacio():
    vacio = [
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
    ]

    assert sudoku.hay_movimientos_posibles(vacio), \
        f'hay_movimientos_posibles(SUDOKU_VACIO) devolvió False'
    
    assert vacio == [
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
        [0, 0, 0,  0, 0, 0,  0, 0, 0],
    ], f'hay_movimientos_posible(SUDOKU_VACIO) modificó el estado pasado por parámetro'

def test_hay_movimientos_posibles_enunciado():
    juego = _obtener_sudoku_enunciado()
    SUDOKU_ENUNCIADO = _obtener_sudoku_enunciado()

    assert sudoku.hay_movimientos_posibles(juego), \
        f'hay_movimientos_posibles(SUDOKU_ENUNCIADO) devolvió False'
    
    assert juego == SUDOKU_ENUNCIADO, \
        f'hay_movimientos_posible(SUDOKU_ENUNCIADO) modificó el estado pasado por parámetro'

def test_hay_movimientos_posibles_resuelto():
    SUDOKU_RESUELTO = [
        [4, 8, 3, 9, 2, 1, 6, 5, 7],
        [9, 6, 7, 3, 4, 5, 8, 2, 1],
        [2, 5, 1, 8, 7, 6, 4, 9, 3],
        [5, 4, 8, 1, 3, 2, 9, 7, 6],
        [7, 2, 9, 5, 6, 4, 1, 3, 8],
        [1, 3, 6, 7, 9, 8, 2, 4, 5],
        [3, 7, 2, 6, 8, 9, 5, 1, 4],
        [8, 1, 4, 2, 5, 3, 7, 6, 9],
        [6, 9, 5, 4, 1, 7, 3, 8, 2]
    ]

    assert not sudoku.hay_movimientos_posibles(SUDOKU_RESUELTO), \
        f'hay_movimientos_posibles(SUDOKU_RESUELTO) devolvió Verdadero'
    
    assert SUDOKU_RESUELTO == [
        [4, 8, 3, 9, 2, 1, 6, 5, 7],
        [9, 6, 7, 3, 4, 5, 8, 2, 1],
        [2, 5, 1, 8, 7, 6, 4, 9, 3],
        [5, 4, 8, 1, 3, 2, 9, 7, 6],
        [7, 2, 9, 5, 6, 4, 1, 3, 8],
        [1, 3, 6, 7, 9, 8, 2, 4, 5],
        [3, 7, 2, 6, 8, 9, 5, 1, 4],
        [8, 1, 4, 2, 5, 3, 7, 6, 9],
        [6, 9, 5, 4, 1, 7, 3, 8, 2]
    ], f'hay_movimientos_posible(SUDOKU_RESUELTO) modificó el estado pasado por parámetro'


# Sólo se van a correr aquellos tests que estén mencionados dentro de esta constante
TESTS = (
    test_crear_juego_representacion_enunciado,
    test_crear_juego_todos_cero,
    test_hay_valor_en_fila_devuelve_verdadero,
    test_hay_valor_en_fila_devuelve_falso,
    test_hay_valor_en_columna_devuelve_verdadero,
    test_hay_valor_en_columna_devuelve_falso,
    test_obtener_origen_region,
    test_hay_valor_en_region_devuelve_verdadero,
    test_hay_valor_en_region_devuelve_falso,
    test_es_movimiento_valido_vacio_es_invalido,
    test_es_movimiento_valido_solucion_son_validos,
    test_es_movimiento_valido_enunciado_son_invalidos,
    test_insertar_valor_valido,
    test_insertar_valor_solucion_completa,
    test_insertar_valor_enunciado_devuelve_mismo_estado,
    test_insertar_valor_invalido_devuelve_mismo_estado,
    test_borrar_valor,
    test_esta_terminado_sin_resolver,
    test_esta_terminado_resuelto,
    test_obtener_valor,
    test_hay_movimientos_posibles_vacio,
    test_hay_movimientos_posibles_enunciado,
    test_hay_movimientos_posibles_resuelto
)

# El código que viene abajo tiene algunas *magias* para simplificar la corrida
# de los tests y proveer la mayor información posible sobre los errores que se
# produzcan. ¡No te preocupes si no lo entendés completamente!

# Colores ANSI para una salida más agradable en las terminales que lo permitan
COLOR_OK = '\033[1m\033[92m'
COLOR_ERR = '\033[1m\033[91m'
COLOR_RESET = '\033[0m'


def print_color(color: str, *args, **kwargs):
    '''
    Mismo comportamiento que `print` pero con un
    primer parámetro para indicar de qué color se
    imprimirá el texto.

    Si la constante TERMINAL_SIN_COLOR es True,
    esta función será exactamente equivalente
    a utilizar `print`.
    '''
    if TERMINAL_SIN_COLOR:
        print(*args, **kwargs)
    else:
        print(color, end='')
        print(*args, **kwargs)
        print(COLOR_RESET, end='', flush=True)

import sys
def main():
    tests_fallidos = []
    tests_a_correr = [int(t) for t in sys.argv[1:]]
    for i, test in [(i,test) for i,test in enumerate(TESTS) if not tests_a_correr or i+1 in tests_a_correr]:
        print(f'Prueba {i + 1 :02} - {test.__name__}: ', end='', flush=True)
        try:
            test()   
            print_color(COLOR_OK, '[OK]')
        except AssertionError as e:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, '[ERROR]')
            print_color(COLOR_ERR, ' >', *e.args)
        except Exception as e:
            tests_fallidos.append(test.__name__)
            print_color(COLOR_ERR, '[BOOM - Explotó]')
            print('\n--------------- Python dijo: ---------------')
            traceback.print_exc()
            print('--------------------------------------------\n')

            
            
    if not tests_fallidos:
        print()
        print_color(COLOR_OK, '###########')
        print_color(COLOR_OK, '# TODO OK #')
        print_color(COLOR_OK, '###########')
        print()
    else:
        print()
        print_color(COLOR_ERR, '##################################')
        print_color(COLOR_ERR, '              ¡ERROR!             ')
        print_color(COLOR_ERR, 'Los siguientes tests fallaron:')
        for test_con_error in tests_fallidos:
            print_color(COLOR_ERR, ' - ' + test_con_error)
        print_color(COLOR_ERR, '##################################')
        print('TIP: Revisá el código de las pruebas que fallaron en el archivo sudoku-test.py.')

main()