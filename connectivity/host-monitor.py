#!/usr/bin/env python3
# ==========================================================
# SCRIPT: Monitoramento de Conectividade em Lote (Ping)
#
# Objetivo:
#   Verificar a conectividade de múltiplos IPs ou hostnames
#   através de testes ICMP (ping), registrando os resultados
#   em arquivo de log.
#
# Cenário:
#   Utilizado para:
#   - Monitoramento básico de servidores e dispositivos
#   - Teste rápido de conectividade de rede
#   - Verificação de disponibilidade de hosts
#   - Diagnóstico inicial antes de troubleshooting avançado
#
# Funcionamento:
#   - Lê lista de hosts a partir de arquivo local
#   - Cria diretório de logs automaticamente
#   - Define quantidade de pings e timeout por host
#   - Executa comando ping via subprocess
#   - Identifica hosts como UP ou DOWN com base no retorno
#   - Registra resultados em log com data
#   - Exibe resumo final com total de hosts ativos/inativos
#
# Diferencial Técnico:
#   - Uso de subprocess para execução de ping (contorna limitação de raw socket)
#   - Controle de quantidade de pacotes e timeout
#   - Função de log estilo "tee" (terminal + arquivo)
#   - Contabilização de hosts UP/DOWN
#   - Estrutura simples e eficiente para monitoramento em lote
#
# Autor: Francklin Leandro
# Data: 31/03/2026
#
# Requisitos:
#   - python 3
#   - utilitário ping disponível no sistema
#   - Biblioteca os
#   - Biblioteca datetime
#   - Biblioteca subprocess
#
# Arquivo de Entrada:
#   $HOME/rede/lista_hosts.txt
#
# Diretório de Logs:
#   $HOME/rede/logs
#
# Uso:
#   ./host-monitor.py
# ==========================================================

import os
# Manipula arquivos, diretórios e ambiente do sistema.
import datetime
# Manipula datas e horas.
import subprocess
# Permite executar comandos do sistema operacional (como ping)

# Arquivo de entrada
ARQUIVO_HOSTS = os.path.join(os.environ["HOME"], "rede", "lista_hosts.txt")
# Caminho completo do arquivo com lista de hosts

# Diretório de logs
DIRETORIO_LOG = os.path.join(os.environ["HOME"], "rede", "logs")

# Data atual
DATA_ATUAL = datetime.datetime.now().strftime("%d-%m-%Y")

ARQUIVO_LOG = os.path.join(DIRETORIO_LOG, f"ping_{DATA_ATUAL}.log")

# Configuração do ping
QTD_PING = 3
# Quantidade de pacotes ICMP enviados por host

TIMEOUT = 2
# Tempo máximo de espera por resposta (em segundos)

# Verifica se o arquivo existe
if not os.path.isfile(ARQUIVO_HOSTS):
# Garante que a lista de hosts existe antes de executar

    print(f"ERRO: Arquivo {ARQUIVO_HOSTS} não encontrado.")

    exit(1)
    # Sai do script

os.makedirs(DIRETORIO_LOG, exist_ok=True)
# Cria diretório caso não exista (sem erro se já existir)

HOSTS_UP = 0
# Conta hosts que responderam ao ping

HOSTS_DOWN = 0
# Conta hosts que não responderam

# Função tipo "tee"
def log_print(mensagem):
# Função para imprimir e salvar no log ao mesmo tempo

    print(mensagem)

    with open(ARQUIVO_LOG, "a") as log:
    # Abre o arquivo no modo append

        log.write(mensagem + "\n")
        # Escreve a mensagem no log
        # Escreve no arquivo de log (sem sobrescrever)

print("==============================================")
print(" INICIANDO MONITORAMENTO DE CONECTIVIDADE")
print(f" Data/Hora: {datetime.datetime.now()}")
print("==============================================\n")

# Leitura dos hosts linha a linha
with open(ARQUIVO_HOSTS, "r") as arquivo:
# Abre o arquivo contendo os hosts

    for linha in arquivo:
    # Itera linha por linha

        HOST = linha.strip()
        # Remove espaços e quebras de linha

        # Ignora linhas inválidas
        if not HOST or HOST.startswith("#"):
        # Evita linhas vazias ou comentários

            continue
            # Pula para o próximo host

        print(f"\nTestando conectividade com: {HOST}")
        # Exibe no terminal o host atual

        # Execução do ping
        resultado = subprocess.run(
        # Executa comando externo "ping"

            ["ping", "-c", str(QTD_PING), "-W", str(TIMEOUT), HOST],
            # -c = quantidade de pacotes | -W = timeout por resposta

            stdout=subprocess.DEVNULL,
            # Descarta saída padrão (não polui terminal)

            stderr=subprocess.DEVNULL
            # Descarta erros do comando
        )

        data_log = datetime.datetime.now().strftime("%Y-%m-%d")
        # Data formatada para registro no log

        if resultado.returncode == 0:
        # Código 0 indica sucesso (host respondeu)

            log_print(f"{data_log} - {HOST} - UP")

            HOSTS_UP += 1
            # Incrementa contador de hosts ativos

        else:
        # Qualquer outro código indica falha

            log_print(f"{data_log} - {HOST} - DOWN")

            HOSTS_DOWN += 1
            # Incrementa contador de hosts inativos

print("\n==============================================")
print(" RESUMO DO MONITORAMENTO")
print("==============================================")
print(f" Hosts com resposta : {HOSTS_UP}")
print(f" Hosts sem resposta : {HOSTS_DOWN}")
print(f" Log gerado em      : {ARQUIVO_LOG}")
print("==============================================")
