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

def arbol(A, B):
    """Calcula la diferencia simétrica de dos conjuntos."""
    R = []
    for i in A:
        for x in B:
            R.append((i, x))  # Cambiar a tuplas para que se vea como un conjunto
    return set(R)  # Convertir la lista en un conjunto

# Diccionario para almacenar los conjuntos
conjuntos = {}
universal = set()

def evaluar_expresion(expresion):
    """Evalúa una expresión de operaciones entre conjuntos."""
    try:
        # Crear un entorno seguro con las funciones y conjuntos disponibles
        entorno = {
            "union": union,
            "interseccion": interseccion,
            "diferencia": diferencia,
            "complemento": complemento,
            **conjuntos,  # Agregar los conjuntos definidos por el usuario
            "universal": universal  # Agregar el conjunto universal
        }

        # Evaluar la expresión en el entorno seguro
        resultado = eval(expresion, {"__builtins__": None}, entorno)
        return resultado
    except Exception as e:
        # Manejar errores en caso de que la expresión sea inválida
        print(f"Error: {e}")
        return None

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        # Añadir conjunto
        nombre = input("Nombre del conjunto: ")
        if nombre in conjuntos:
            print("El nombre ya existe. Intenta con otro.")
        else:
            contenido = input("Elementos del conjunto (separados por comas): ")
            elementos = set(contenido.split(","))
            conjuntos[nombre] = elementos
            universal.update(elementos)  # Actualizar el conjunto universal
            print(f"Conjunto '{nombre}' agregado.")
    
    elif opcion == "2":
        # Ver conjuntos
        print("\nConjuntos almacenados:")
        for nombre, contenido in conjuntos.items():
            print(f"{nombre}: {contenido}")
        print(f"\nConjunto Universal: {universal}")
    
    elif opcion == "3":
        # Realizar operaciones entre conjuntos
        print("\nConjuntos disponibles:")
        for nombre, contenido in conjuntos.items():
            print(f"{nombre}: {contenido}")
        print(f"universal: {universal}")
        
        print("\nOperaciones disponibles:")
        print("Usa los nombres de los conjuntos y los operadores:")
        print("|: Unión, &: Intersección, -: Diferencia, complemento(A): Complemento")
        print("Ejemplo: union(A, complemento(B)), interseccion(A, diferencia(C, D))")
        
        expresion = input("Ingresa la expresión: ")
        resultado = evaluar_expresion(expresion)
        
        if resultado is not None:
            # Guardar el resultado con un nombre basado en la operación
            nombre_resultado = f"Resultado_{expresion.replace(' ', '')}"
            conjuntos[nombre_resultado] = resultado
            print(f"Resultado guardado como '{nombre_resultado}': {resultado}")
    
    elif opcion == "4":
        # Generar árbol
        print("\nConjuntos disponibles:")
        for nombre, contenido in conjuntos.items():
            print(f"{nombre}: {contenido}")
        
        conjunto1 = input("Ingresa el nombre del primer conjunto: ")
        conjunto2 = input("Ingresa el nombre del segundo conjunto: ")
        
        if conjunto1 in conjuntos and conjunto2 in conjuntos:
            resultado_arbol = arbol(conjuntos[conjunto1], conjuntos[conjunto2])
            print("\nResultado del árbol:")
            print(resultado_arbol)  # Imprimir como un conjunto
        else:
            print("Uno o ambos conjuntos no existen. Intenta de nuevo.")
    
    elif opcion == "5":
        # Salir del programa
        print("Saliendo de la calculadora de conjuntos...")
        break
    
    else:
        print("Opción no válida. Intenta de nuevo.")