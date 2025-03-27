import itertools

def evaluate_logical_expression(expression, values):
    def parse(expr):
        # remueve los parentesis si encapsulan la operacion
        while expr.startswith('(') and expr.endswith(')'): 
            if expr.count('(') == expr.count(')'):
                expr = expr[1:-1]
            else:
                break
        
        # bicondicional
        if '<->' in expr:
            left, right = expr.split('<->', 1)
            return evaluate_logical_equivalence(left, right)
        
        # condicional
        if '->' in expr:
            left, right = expr.split('->', 1)
            return evaluate_logical_implication(left, right)
        
        # disyuncion
        if '|' in expr:
            left, right = expr.split('|', 1)
            return evaluate_logical_or(left, right)
        
        # conjuncion
        if '&' in expr:
            left, right = expr.split('&', 1)
            return evaluate_logical_and(left, right)
        
        # Negacion
        if expr.startswith('¬'):
            return not evaluate_logical_expression(expr[1:], values)
        
        # Base case: otorga las variables en boleanos
        return values.get(expr.strip(), expr.strip() == 'True')

    def evaluate_logical_and(left, right):
        return parse(left.strip()) and parse(right.strip())

    def evaluate_logical_or(left, right):
        return parse(left.strip()) or parse(right.strip())

    def evaluate_logical_implication(left, right):
        left_val = parse(left.strip())
        right_val = parse(right.strip())
        return (not left_val) or right_val

    def evaluate_logical_equivalence(left, right):
        left_val = parse(left.strip())
        right_val = parse(right.strip())
        return left_val == right_val

    return parse(expression)

def generate_extended_truth_table(expression):
    # identifica las variables unicas
    variables = sorted(set(filter(str.isalpha, expression)))
    
    # genera todos los posibles combinaciones de boleanos
    combinations = list(itertools.product([False, True], repeat=len(variables)))
    
    # Preparar encabezados: variables originales y sus negaciones
    headers = []
    for var in variables:
        headers.extend([var, f'¬{var}'])
    headers.append(expression)
    
    # Imprime el encabezado
    header_row = " | ".join(headers)
    print(header_row)
    print("-" * len(header_row))
    
    # Evalua la exprecion de cada combinacion
    for combination in combinations:
        # Crear un diccionario que asigne variables a sus valores boleanos
        values = dict(zip(variables, combination))
        
        # Preparar la fila con variables y sus negaciones
        row_values = []
        for val in combination:
            row_values.extend([int(val), int(not val)])
        
        try:
            # evalua la exprecion
            result = evaluate_logical_expression(expression, values)
            
            # Añade el resultado final
            row_values.append(int(result))
            
            # Convierte la fila a string para imprimir
            row = " | ".join(map(str, row_values))
            print(row)
        
        except Exception as e:
            print(f"Error evaluating expression: {e}")

def main():
    while True:
        print("\n--- Calculadora de Tablas de Verdad Extendida ---")
        print("1. Generar tabla de verdad")
        print("2. Salir")
        
        choice = input("Selecciona una opción (1 o 2): ")
        
        if choice == '1':
            user_input = input("Ingresa una expresión lógica (usa P, Q, R, S, |, &, ¬, ->, <->): ")
            generate_extended_truth_table(user_input)
        elif choice == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, selecciona 1 o 2.")

if __name__ == "__main__":
    main()