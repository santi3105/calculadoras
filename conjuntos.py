def mostrar_menu():
    """Muestra el menú principal."""
    print("\n--- Calculadora de Conjuntos ---")
    print("1.- Añadir conjunto")
    print("2.- Ver conjuntos")
    print("3.- Realizar operaciones entre conjuntos")
    print("4.- Generar árbol")
    print("5.- Salir")
def union(A, B):
    """Calcula la unión de dos conjuntos."""
    return A | B
def interseccion(A, B):
    """Calcula la intersección de dos conjuntos."""
    return A & B
def diferencia(A, B):
    """Calcula la diferencia de dos conjuntos."""
    return A - B
def complemento(A):
    """Calcula el complemento de un conjunto."""
    return universal - A
def subconjunto(A, B):
    """Verifica si A es subconjunto de B y devuelve la intersección si lo es."""
    if B.issubset(A):
        return A & B
    else:
        print(f"{B} no es un subconjunto de {A}")
        return set()
def arbol(A, B):
    """Calcula la diferencia simétrica de dos conjuntos."""
    R = []
    for i in A:
        for x in B:
            R.append((i, x)) 
    return set(R) 

conjuntos = {}
universal = set()

def evaluar_expresion(expresion):
    """Evalúa una expresión de operaciones entre conjuntos."""
    try:
        entorno = {
            "union": union,
            "interseccion": interseccion,
            "diferencia": diferencia,
            "complemento": complemento,
            "subconjunto": subconjunto,
            **conjuntos, 
            "universal": universal 
        }
        resultado = eval(expresion, {"__builtins__": None}, entorno)
        return resultado
    except Exception as e:
        print(f"Error: {e}")
        return None

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")
    if opcion == "1":
        nombre = input("Nombre del conjunto: ")
        if nombre in conjuntos:
            print("El nombre ya existe. Intenta con otro.")
        else:
            contenido = input("Elementos del conjunto (separados por comas): ")
            elementos = set(contenido.split(","))
            conjuntos[nombre] = elementos
            universal.update(elementos) 
            print(f"Conjunto '{nombre}' agregado.")
    elif opcion == "2":
        print("\nConjuntos almacenados:")
        for nombre, contenido in conjuntos.items():
            print(f"{nombre}: {contenido}")
        print(f"\nConjunto Universal: {universal}")
    elif opcion == "3":
        print("\nConjuntos disponibles:")
        for nombre, contenido in conjuntos.items():
            print(f"{nombre}: {contenido}")
        print(f"universal: {universal}")
        print("\nOperaciones disponibles:")
        print("Usa los nombres de los conjuntos y los operadores:")
        print("|: Unión, &: Intersección, -: Diferencia, complemento(A): Complemento, subconjunto(A, B): Subconjunto")
        print("uso del complemento(nombre del conjunto), uso del subconjunto(nombre del conjunto, nombre del otro conjunto)")
        expresion = input("Ingresa la expresión: ")
        resultado = evaluar_expresion(expresion)
        if resultado is not None:
            nombre_resultado = f"Resultado_{expresion.replace(' ', '')}"
            conjuntos[nombre_resultado] = resultado
            print(f"Resultado guardado como '{nombre_resultado}': {resultado}")
    elif opcion == "4":
        print("\nConjuntos disponibles:")
        for nombre, contenido in conjuntos.items():
            print(f"{nombre}: {contenido}")
        conjunto1 = input("Ingresa el nombre del primer conjunto: ")
        conjunto2 = input("Ingresa el nombre del segundo conjunto: ")
        if conjunto1 in conjuntos and conjunto2 in conjuntos:
            resultado_arbol = arbol(conjuntos[conjunto1], conjuntos[conjunto2])
            print("\nResultado del árbol:")
            print(resultado_arbol)
        else:
            print("Uno o ambos conjuntos no existen. Intenta de nuevo.")
    elif opcion == "5":
        print("Saliendo de la calculadora de conjuntos...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")