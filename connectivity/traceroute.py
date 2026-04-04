#!/usr/bin/env python3

# ==========================================================
# SCRIPT: Diagnóstico de Rota de Rede (Traceroute em Lote)
#
# Objetivo:
#   Executar traceroute para múltiplos destinos listados
#   em um arquivo, registrando os resultados em log diário.
#
#
# Observação:
#   - Não existe implementação simples de traceroute em Python puro
#     (exige manipulação de TTL + ICMP/UDP com privilégios)
#   - Portanto, uso de subprocess é necessário
# ==========================================================

import os
import datetime
import subprocess
import shutil

ARQUIVO_DESTINOS = os.path.join(os.environ["HOME"], "rede", "lista_destinos.txt")

DIRETORIO_LOG = os.path.join(os.environ["HOME"], "rede", "logs")

# Data atual
DATA_ATUAL = datetime.datetime.now().strftime("%d-%m-%Y")
ARQUIVO_LOG = os.path.join(DIRETORIO_LOG, f"traceroute_{DATA_ATUAL}.log")

# Número máximo de saltos
MAX_SALTOS = 30

# Verifica se o traceroute está disponível
if shutil.which("traceroute") is None:
    print("ERRO: comando 'traceroute' não encontrado.")
    print("Instale com: sudo apt install traceroute")
    exit(1)

# Verifica arquivo de destinos
if not os.path.isfile(ARQUIVO_DESTINOS):
    print(f"ERRO: Arquivo {ARQUIVO_DESTINOS} não encontrado.")
    exit(1)

# Cria diretório
os.makedirs(DIRETORIO_LOG, exist_ok=True)

# Função para escrever no log e printar (equivalente ao tee)
def log_print(msg):
    print(msg)
    with open(ARQUIVO_LOG, "a") as log:
      # Escreve no arquivo de log (sem sobrescrever)
        log.write(msg + "\n")

log_print("==================================================")
log_print(" DIAGNÓSTICO DE ROTA DE REDE (TRACEROUTE)")
log_print(f" Data: {datetime.datetime.now()}")
log_print("==================================================\n")

# Leitura dos destinos linha a linha
with open(ARQUIVO_DESTINOS, "r") as arquivo:
    for linha in arquivo:
        DESTINO = linha.strip()

         # Ignora linhas vazias ou comentadas
        if not DESTINO or DESTINO.startswith("#"):
            continue
            # Pula para próxima linha

        log_print(f"Destino: {DESTINO}")
        log_print("--------------------------------------------------")

        # Executa traceroute
        resultado = subprocess.run(
            ["traceroute", "-m", str(MAX_SALTOS), DESTINO],
            stdout=subprocess.PIPE,
            # Captura saída padrão para análise
            stderr=subprocess.STDOUT,
            text=True
            # Retorna saída como string (não bytes)
        )

        # Escreve saída completa no log e terminal
        for linha_saida in resultado.stdout.splitlines():
            log_print(linha_saida)

        log_print("")

# Finalização
log_print("==================================================")
log_print(" Diagnóstico concluído.")
log_print(f" Log salvo em: {ARQUIVO_LOG}")
log_print("==================================================")
