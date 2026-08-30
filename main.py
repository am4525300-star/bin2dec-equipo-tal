def bin2dec(binary_str):
    # Validar longitud máxima de 8 dígitos
    if len(binary_str) > 8:
        return "Error: Solo se permiten cadenas de hasta 8 dígitos binarios."
    
    # Validar que solo contenga 0s y 1s
    for char in binary_str:
        if char not in ('0', '1'):
            return "Error: Ingrese únicamente dígitos binarios (0 o 1)."
            
    # Conversión de binario a decimal
    decimal_val = int(binary_str, 2)
    return f"Resultado decimal: {decimal_val}"

if __name__ == "__main__":
    numero = input("Ingrese un número binario (máx 8 dígitos): ")
    print(bin2dec(numero))
