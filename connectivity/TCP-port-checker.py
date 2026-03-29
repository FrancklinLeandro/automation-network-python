Próximo:

#!/usr/bin/env python3
# ==========================================================
# SCRIPT: Verificação de Portas TCP em Hosts de Rede
#
# Objetivo:
#   Testar múltiplas portas TCP em uma lista de hosts,
#   identificando serviços acessíveis e registrando os
#   resultados em arquivo de log.
#
# Cenário:
#   Utilizado para:
#   - Validação rápida de serviços ativos (SSH, HTTP, HTTPS, DNS)
#   - Auditoria básica de exposição de portas
#   - Troubleshooting de conectividade entre hosts
#   - Substituição leve de ferramentas como netcat
#
# Funcionamento:
#   - Lê lista de hosts a partir de arquivo local
#   - Define conjunto de portas TCP a serem testadas
#   - Cria diretório de logs automaticamente
#   - Implementa função de log (print + arquivo)
#   - Para cada host:
#       - Valida entrada (ignora comentários e linhas vazias)
#       - Testa conexão TCP via socket
#       - Identifica portas abertas, fechadas ou inacessíveis
#       - Trata erros de DNS e exceções de rede
#   - Registra resultados em log com data
#
# Diferencial Técnico:
#   - Uso da biblioteca socket (dispensa ferramentas externas)
#   - Controle de timeout por conexão
#   - Tratamento de exceções de rede e DNS
#   - Função de log semelhante ao comportamento do "tee"
#   - Estrutura simples e portátil (sem dependências externas)
#
# Autor: Francklin Leandro
# Data: 29/03/2026
#
# Requisitos:
#   - python 3
#   - Biblioteca os
#   - Biblioteca socket
#   - Biblioteca datetime
#
# Arquivo de Entrada:
#   os.path.join(os.environ["HOME"], "rede", "lista_hosts.txt")
#
# Diretório de Logs:
#   os.path.join(os.environ["HOME"], "rede", "logs")
#
# Uso:
#   ./TCP-port-checker.py
# ==========================================================

import os
import socket
import datetime

# Arquivo com lista de hosts
ARQUIVO_HOSTS = os.path.join(os.environ["HOME"], "rede", "lista_hosts.txt")

# Lista de portas TCP
PORTAS_TCP = [22, 80, 443, 53]

# Timeout (segundos)
TIMEOUT = 3

# Diretório e arquivo de log
DIRETORIO_LOG = os.path.join(os.environ["HOME"], "rede", "logs")
DATA_ATUAL = datetime.datetime.now().strftime("%d-%m-%Y")
ARQUIVO_LOG = os.path.join(DIRETORIO_LOG, f"portas_{DATA_ATUAL}.log")

# Verifica se o arquivo existe
if not os.path.isfile(ARQUIVO_HOSTS):
    print(f"ERRO: Arquivo {ARQUIVO_HOSTS} não encontrado.")
    exit(1)

# Cria diretório de log
os.makedirs(DIRETORIO_LOG, exist_ok=True)

# Função para escrever no log e printar (equivalente ao tee)
def log_print(mensagem):
    print(mensagem)
    with open(ARQUIVO_LOG, "a") as log:
        log.write(mensagem + "\n")

# Cabeçalho
print("====================================================")
print(" VERIFICAÇÃO DE PORTAS TCP EM HOSTS DE REDE")
print(f" Data: {datetime.datetime.now()}")
print("==================================================\n")

with open(ARQUIVO_LOG, "a") as log:
    log.write("==================================================\n")
    log.write(" VERIFICAÇÃO DE PORTAS TCP EM HOSTS DE REDE\n")
    log.write(f" Data: {datetime.datetime.now()}\n")
    log.write("==================================================\n\n")

# Leitura dos hosts
with open(ARQUIVO_HOSTS, "r") as arquivo:
    for linha in arquivo:
        HOST = linha.strip()

        # Ignora linhas vazias ou comentadas
        if not HOST or HOST.startswith("#"):
            continue

        log_print(f"Host: {HOST}")

        # Testa cada porta
        for PORTA in PORTAS_TCP:

            # Cria socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(TIMEOUT)

            try:
                resultado = sock.connect_ex((HOST, PORTA))
                # connect_ex retorna 0 se conectou com sucesso

                if resultado == 0:
                    log_print(f"  Porta {PORTA}/TCP: ABERTA")
                else:
                    log_print(f"  Porta {PORTA}/TCP: FECHADA ou INACESSÍVEL")

            except socket.gaierror:
                # Erro de resolução de nome (DNS)
                log_print(f"  Porta {PORTA}/TCP: HOST INVÁLIDO")

            except Exception as e:
                # Qualquer outro erro de rede
                log_print(f"  Porta {PORTA}/TCP: ERRO ({e})")

            finally:
                sock.close()

        log_print("--------------------------------------------------")

# Finalização
print("\nVerificação concluída.")
print(f"Log salvo em: {ARQUIVO_LOG}")
