#!/usr/bin/env python3

# ==========================================================
# SCRIPT: Teste de Conectividade (Ping) de Switches em Lote
#
# Objetivo:
#   Verificar a disponibilidade (UP/DOWN) de múltiplos switches
#   listados em arquivos CSV, gerando relatório consolidado em log.
#
# Cenário:
#   Utilizado em ambientes corporativos para:
#   - Verificação rápida de disponibilidade de switches por site
#   - Validação de falhas após quedas de energia
#   - Checagem matinal de infraestrutura
#   - Apoio a troubleshooting de indisponibilidade
#
# Funcionamento:
#   - Lê todos os arquivos .csv de um diretório específico
#   - Ignora linhas vazias ou comentadas (#)
#   - Extrai NOME, IP, SITE e MODELO
#   - Executa ping com 2 tentativas e timeout de 2 segundos
#   - Classifica o switch como UP ou DOWN
#   - Gera log diário formatado
#
# Autor: Francklin Leandro
# Data: 04/03/2026
#
# Requisitos:
#   - python
#   - ping(Subprocess)
#   - Biblioteca subprocess
#   - Biblioteca os
#   - Biblioteca glob
#   - Biblioteca datetime
#
# Diretório de Entrada:
#   os.path.expanduser("~/PINGS/ARQUIVOS_SWITCH")
#
# Diretório de Log:
#   os.path.expanduser(f"~/PINGS/LOG_SWITCH)
#
# Saída:
#   Relatório no formato:
#   NOME; IP; SITE; MODELO; STATUS
#
# Uso:
#   ./switch-csv.py
# ==========================================================

import os
import glob
import datetime
import subprocess

# Diretório onde estão os CSVs dos switches
DIRETORIO_SWITCHES = os.path.expanduser("~/PINGS/ARQUIVOS_SWITCH")

# Lista de arquivos .csv (equivalente ao nullglob do Bash)
ARQUIVOS_SWITCHES = glob.glob(os.path.join(DIRETORIO_SWITCHES, "*.csv"))

data_atual = datetime.datetime.now().strftime("%d-%m-%Y")
LOG = os.path.expanduser(f"~/PINGS/LOG_SWITCH/switch_{data_atual}.log")

# Garante que o diretório de log exista
os.makedirs(os.path.dirname(LOG), exist_ok=True)

with open(LOG, "w") as log:
    linha = f"\n------ DATA: {data_atual} ------"
    print(linha)
    log.write(linha + "\n")

    cabecalho = "\nNOME; IP; SITE; MODELO; STATUS"
    print(cabecalho)
    log.write(cabecalho + "\n")

    inicio = "\n------ INICIANDO TESTE DE PING DOS SWITCHES ------"
    print(inicio)
    log.write(inicio + "\n\n")

    # Percorre cada arquivo CSV encontrado
    for arquivo in ARQUIVOS_SWITCHES:

        # Verifica se o item realmente é um arquivo regular
        # Caso não seja, pula para o próximo arquivo
        if not os.path.isfile(arquivo):
            continue

        with open(arquivo, "r") as f:
            linhas = f.readlines()
             # Exibe o conteúdo do arquivo CSV no terminal 

        for linha_csv in linhas:
            linha_csv = linha_csv.strip()
            # Remove espaços e quebras de linha no início/fim

            # Ignora linhas vazias ou comentadas
            if not linha_csv or linha_csv.startswith("#"):
                continue

            try:
                nome, ip, site, modelo = linha_csv.split(";")
                # Extrai as 4 colunas: nome, IP, site e modelo
                # Divide os campos separados por ';'
            except ValueError:
                # Linha malformada → ignora
                continue

            # Executa ping (2 pacotes, timeout 2s)
            resultado = subprocess.run(
                ["ping", "-c", "2", "-W", "2", ip.strip()],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if resultado.returncode == 0:
                status = "UP"
            else:
                status = "DOWN"

            saida = f"{nome.strip()}; {ip.strip()}; {site.strip()}; {modelo.strip()}; {status}"
            print(saida)
            log.write(saida + "\n\n")
            # Exibe o nome, ip, site, modelo e status dos switches
            # Escreve resultado no log e mostra no terminal
            # .strip() remove espaços, tabs e quebras de linha das extremidades de cada campo individual(nome, ip, etc)

    fim = "\n------ TESTE FINALIZADO ------"
    print(fim)
    log.write(fim + "\n")
