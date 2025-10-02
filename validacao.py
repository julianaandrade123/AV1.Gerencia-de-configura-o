def validar_vetores(v1, v2):
    if not v1 or not v2:
        raise ValueError("Nenhum dos vetores pode ser vazio.")
    if len(v1) != len(v2):
        raise ValueError("Os vetores devem ter o mesmo número de dimensões.")
    if not all(isinstance(x, (int, float)) for x in v1 + v2):
        raise ValueError("Todos os elementos devem ser números.")
    return True