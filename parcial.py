def contar_letras_a(string):
    contador = 0
    for letra in string:
        if letra == 'a' or letra == 'A':
            contador += 1
    return contador

# Ejemplo de uso
texto = "Hola Amigo"
cantidad_a = contar_letras_a(texto)
print("La cantidad de letras 'a' o 'A' en el texto es:", cantidad_a)
