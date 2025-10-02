# Produto escalar entre dois vetores
vetor1 = list(map(float, input("Digite os elementos do primeiro vetor (separados por vírgula): ").split(',')))
vetor2 = list(map(float, input("Digite os elementos do segundo vetor (separados por vírgula): ").split(',')))

if len(vetor1) != len(vetor2):
    print("Erro: os vetores devem ter o mesmo tamanho.")
else:
    produto = sum(v1 * v2 for v1, v2 in zip(vetor1, vetor2))
    print(f"Produto escalar: {produto}")