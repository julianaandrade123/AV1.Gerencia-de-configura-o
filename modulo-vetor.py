import math

def calcular_modulo_vetor(vetor):
    """Calcula o módulo (norma euclidiana) de um vetor."""
    
    # Verifica se a entrada é uma lista ou tupla (simples)
    if not isinstance(vetor, (list, tuple)):
        raise ValueError("A entrada deve ser um vetor (lista ou tupla de números).")
        
    # 1. Soma do quadrado de cada componente
    soma_dos_quadrados = sum(x**2 for x in vetor)
    
    # 2. Retorna a raiz quadrada da soma
    modulo = math.sqrt(soma_dos_quadrados)
    
    return modulo

# Exemplo de uso 
if __name__ == '__main__':
    vetor_teste = [3, 4]
    resultado = calcular_modulo_vetor(vetor_teste)
    print(f"O módulo do vetor {vetor_teste} é: {resultado}")
