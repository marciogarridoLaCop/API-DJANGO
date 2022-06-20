
def temperarura_valida(valor_temperatura):
    return valor_temperatura.isalpha()

def temperarura_tamanho(valor_temperatura):
    return len(valor_temperatura) <= 5

def umidade_valida(valor_umidade):
    return valor_umidade.isalpha()

def pressao_valida(valor_pressao):
    return valor_pressao.isalpha()