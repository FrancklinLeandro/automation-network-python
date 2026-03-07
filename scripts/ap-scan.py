#!/usr/bin/env python3

# ==========================================================
# SCRIPT: Monitoramento de Access Points (APs)
#
# Objetivo:
#   Verificar a conectividade de múltiplos Access Points
#   realizando teste ICMP (ping) e registrando os resultados
#   em log estruturado.
#
# Cenário:
#   Utilizado para:
#   - Monitoramento diário de APs
#   - Verificação rápida de indisponibilidade
#   - Auditoria de conectividade Wi-Fi
#   - Controle operacional de infraestrutura wireless
#
# Funcionamento:
#   - Cria diretório de logs automaticamente
#   - Lê arquivo estruturado contendo:
#       NOME_AP HOST IP
#   - Ignora linhas vazias ou comentadas (#)
#   - Executa ping configurável por IP
#   - Registra status UP/DOWN em log
#   - Exibe resumo final da execução
#
# Diferencial Técnico:
#   - Log diário com data automática
#   - Contadores de disponibilidade
#   - Estrutura preparada para integração com planilhas
#
# Autor: Francklin Leandro
# Data: 04/03/2026
#
# Requisitos:
#   - python
#   - ping(Subprocess)
#   - Biblioteca os
#   - Biblioteca subprocess
#   - Biblioteca datetime
#
# Arquivo de Entrada:
#   os.path.join(os.environ["HOME"], "PINGS", "ARQUIVOS_AP", "lista_APs.txt")
#
# Estrutura do Arquivo:
#   NOME_AP HOST IP
#
# Diretório de Logs:
#   os.path.join(os.environ["HOME"], "PINGS", "LOG_AP")
#
# Uso:
#   ./ap-scan.py
# ==========================================================

import os
import subprocess
import datetime

LOG_DIR = os.path.join(os.environ["HOME"], "PINGS", "LOG_AP")
os.makedirs(LOG_DIR, exist_ok=True)

# Arquivo contendo: NOME_AP HOST IP
ARQUIVO_APS = os.path.join(os.environ["HOME"], "PINGS", "ARQUIVOS_AP", "lista_APs.txt")

# Data atual no formato dia-mês-ano
DATA_ATUAL = datetime.datetime.now().strftime("%d-%m-%Y")

# Arquivo de log com data atual
LOG = os.path.join(LOG_DIR, f"ap_{DATA_ATUAL}.log")

print(f"\n------ DATA: {DATA_ATUAL} ------")
with open(LOG, "w", encoding="utf-8") as f:
    f.write(f"\n------ DATA: {DATA_ATUAL} ------\n")

print("NOME_AP; HOST; IP; STATUS")
with open(LOG, "a", encoding="utf-8") as f:
    f.write("NOME_AP; HOST; IP; STATUS\n")

print("\n------ INICIANDO VERIFICAÇÃO DOS APs ------")
with open(LOG, "a", encoding="utf-8") as f:
    f.write("\n------ INICIANDO VERIFICAÇÃO DOS APs ------\n\n")

# Lê o arquivo linha a linha
with open(ARQUIVO_APS, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()

        # Ignora linhas vazias ou comentadas
        if not linha or linha.startswith("#"):
            continue

        # Evita que o script quebre caso uma linha do arquivo não esteja no formato esperado
        try:
            NOME_AP, HOST, IP = linha.split()
        except ValueError:
            # Linha inválida (não possui exatamente 3 campos)
            # Quando uma linha está no formato inválido, ela é ignorada e o script continua sem quebrar
            continue

        # Testa conectividade (ping)
        resultado = subprocess.run(
            ["ping", "-c", "3", "-W", "3", IP],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if resultado.returncode == 0:
            STATUS = "UP"
        else:
            STATUS = "DOWN"

        # Exibe no terminal
        print(f"{NOME_AP}; {HOST}; {IP}; {STATUS}")
        print("")

        # Grava no log
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(f"{NOME_AP}; {HOST}; {IP}; {STATUS}\n\n")

# Finalização
print("\n------ VERIFICAÇÃO CONCLUÍDA ------")
with open(LOG, "a", encoding="utf-8") as f:
    f.write("\n------ VERIFICAÇÃO CONCLUÍDA ------\n")
