import numpy as np

# Função para ler um vetor de 3 elementos
def ler_vetor(nome):
    while True:
        try:
            valores = list(map(float, input(f"Digite os 3 elementos do vetor {nome} separados por espaço: ").split()))
            if len(valores) != 3:
                print("Você deve digitar exatamente 3 números.")
                continue
            return np.array(valores)
        except ValueError:
            print("Entrada inválida. Digite apenas números separados por espaço.")

# Leitura dos vetores
a = ler_vetor('a')
b = ler_vetor('b')
c = ler_vetor('c')

# Produto vetorial entre b e c
vetorial = np.cross(b, c)

# Produto misto: a · (b × c)
produto_misto = np.dot(a, vetorial)

# Resultado
print(f"\nProduto Misto: {produto_misto}")