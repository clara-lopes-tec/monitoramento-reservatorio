import colorama
import random
from colorama import Fore, Style

# Inicializa o colorama 
colorama.init(autoreset=True)

def obter_estilo(nivel):
    """Função responsável por definir a cor e a mensagem conforme o nível."""
    # Lista de dicionários para organização dos dados
    dados_niveis = {
        1: (Fore.RED, "Muito baixo (crítico)"),
        2: (Fore.YELLOW, "Baixo"),
        3: (Fore.GREEN, "Médio"),
        4: (Fore.CYAN, "Alto"),
        5: (Fore.BLUE, "Muito alto (alerta)")
    }
    return dados_niveis.get(nivel, (Fore.WHITE, "Nível Inválido"))

def monitoramento():
    # 1. Exibição da Tabela de Referência (A Lista)
    print("TABELA DE REFERÊNCIA DE NÍVEIS")
    for i in range(1, 6):
        cor, mensagem = obter_estilo(i)
        print(f"Nível {i}: {cor}{mensagem}")


    # 2. Exibição da Situação atual
    # Definição de qual o nível o reservatório está marcando
    nivel_atual = random.randint(1, 5)
    cor_atual, msg_atual = obter_estilo(nivel_atual)

    print("LEITURA DO RESERVATÓRIO ATUAL")
    print(f"STATUS: {cor_atual}{msg_atual}")
    
    # 3. Restaurar estilo padrão 
    print(Style.RESET_ALL)

if __name__ == "__main__":
    monitoramento()