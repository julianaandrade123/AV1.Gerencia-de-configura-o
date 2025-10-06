def validar_vetor(vetor):
    if len(vetor) not in [2, 3]:
        raise ValueError("O vetor deve ter 2 ou 3 elementos.")
    return vetor

# Testando a função
try:
    vetor = [1, 2, 3]
    print(validar_vetor(vetor))
except ValueError as e:
    print(e)