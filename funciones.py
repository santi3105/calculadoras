def conjunto_operaciones(conjuntos: list):
    resultado = {}
    union_total = set.union(*conjuntos)
    interseccion_total = set.intersection(*conjuntos)

    resultado['Union'] = union_total
    resultado['Interseccion'] = interseccion_total

    for i, A in enumerate(conjuntos):
        for j, B in enumerate(conjuntos):
            if i != j:
                resultado[f'Diferencia_{i+1}_{j+1}'] = A - B
                resultado[f'Diferencia_{j+1}_{i+1}'] = B - A
                resultado[f'Diferencia_Simetrica_{i+1}_{j+1}'] = A ^ B

    return resultado


n = int(input("Ingrese el número de conjuntos: "))
conjuntos = []

for i in range(n):
    elementos = set(input(f"Ingrese los elementos del conjunto {i+1} separados por espacio: ").split())
    conjuntos.append(elementos)

resultado = conjunto_operaciones(conjuntos)
print("\nResultados:")
for operacion, valor in resultado.items():
    print(f"{operacion}: {valor}")
    
