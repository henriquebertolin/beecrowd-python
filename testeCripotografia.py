def primeira_passada(texto):
    resultado = ''
    for char in texto:
        if char.isalpha():
            novo_char = chr((ord(char) - ord('a' if char.islower() else 'A' ) + 3) % 26 + ord('a' if char.islower() else 'A'))
            resultado += novo_char
        else:
            resultado += char
    return resultado

def segunda_passada(texto):
    return texto[::-1]

def terceira_passada(texto):
    metade = len(texto) // 2
    resultado = list(texto)
    for i in range(metade, len(texto)):
        char = resultado[i]
        if char.isalpha():
            novo_char = chr((ord(char) - ord('a' if char.islower() else 'A' ) - 1) % 26 + ord('a' if char.islower() else 'A'))
            resultado[i] = novo_char
    return ''.join(resultado)

def criptografar(texto):
    texto = primeira_passada(texto)
    texto = segunda_passada(texto)
    texto = terceira_passada(texto)
    return texto

n = int(input())

for _ in range(n):
    linha = input()
    linha_criptografada = criptografar(linha)
    print(linha_criptografada)
