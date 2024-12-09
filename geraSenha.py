import random
import string

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_numeros=True, incluir_especiais=True):
    """
    Gera uma senha segura com base nos critérios fornecidos, garantindo que pelo menos
    um dos tipos de caracteres escolhidos esteja presente.
    
    :param tamanho: Tamanho da senha (padrão: 12)
    :param incluir_maiusculas: Incluir letras maiúsculas (padrão: True)
    :param incluir_numeros: Incluir números (padrão: True)
    :param incluir_especiais: Incluir caracteres especiais (padrão: True)
    :return: Uma senha gerada aleatoriamente
    """
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser no mínimo 4 para garantir segurança.")
    
    # Conjuntos de caracteres
    caracteres = string.ascii_lowercase  # Letras minúsculas
    obrigatorios = []  # Armazena pelo menos um caractere de cada tipo escolhido
    
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
        obrigatorios.append(random.choice(string.ascii_uppercase))
    if incluir_numeros:
        caracteres += string.digits
        obrigatorios.append(random.choice(string.digits))
    if incluir_especiais:
        caracteres += "!@#$%^&*()-_=+[]{}|;:,.<>?/~`"
        obrigatorios.append(random.choice("!@#$%^&*()-_=+[]{}|;:,.<>?/~`"))
    
    # Gera o restante da senha
    restante = tamanho - len(obrigatorios)
    senha = ''.join(random.choice(caracteres) for _ in range(restante))
    
    # Adiciona os caracteres obrigatórios e embaralha
    senha += ''.join(obrigatorios)
    senha = ''.join(random.sample(senha, len(senha)))
    
    return senha

# Exemplo de uso
if __name__ == "__main__":
    tamanho = int(input("Digite o tamanho da senha: "))
    incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
    incluir_numeros = input("Incluir números? (s/n): ").strip().lower() == 's'
    incluir_especiais = input("Incluir caracteres especiais? (s/n): ").strip().lower() == 's'
    
    senha = gerar_senha(
        tamanho=tamanho,
        incluir_maiusculas=incluir_maiusculas,
        incluir_numeros=incluir_numeros,
        incluir_especiais=incluir_especiais
    )
    
    print(f"Senha gerada: {senha}")
