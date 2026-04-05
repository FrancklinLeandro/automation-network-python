#!/usr/bin/env python3
# ==========================================================
# SCRIPT: Monitoramento de Latência e Perda de Pacotes
#
# Objetivo:
#   Medir latência média e percentual de perda de pacotes
#   para múltiplos destinos, auxiliando na análise de
#   qualidade de rede.
#
# Cenário:
#   Utilizado para:
#   - Monitoramento de links WAN
#   - Diagnóstico de instabilidade de rede
#   - Verificação de qualidade de conexão com serviços críticos
#   - Coleta de evidências para troubleshooting
#
# Funcionamento:
#   - Lê lista de destinos a partir de arquivo local
#   - Cria diretório de logs automaticamente
#   - Define quantidade de pacotes e intervalo entre pings
#   - Executa comando ping via subprocess capturando saída
#   - Analisa saída do ping utilizando expressões regulares
#   - Extrai percentual de perda de pacotes
#   - Extrai latência média (RTT avg)
#   - Registra resultados formatados em log
#
# Diferencial Técnico:
#   - Parsing da saída do ping em Python (dispensa grep/awk)
#   - Uso de regex para extração de métricas
#   - Captura completa da saída do comando para análise
#   - Estrutura adaptável para monitoramento contínuo
#   - Geração de log estruturado para auditoria
#
# Autor: Francklin Leandro
# Data: 01/04/2026
#
# Requisitos:
#   - python 3
#   - utilitário ping disponível no sistema
#   - Biblioteca os
#   - Biblioteca datetime
#   - Biblioteca subprocess
#   - Biblioteca re
#
# Arquivo de Entrada:
#   $HOME/rede/lista_destinos.txt
#
# Diretório de Logs:
#   $HOME/rede/logs
#
# Uso:
#   ./latency-monitor.py
# ==========================================================

import os
# Manipula arquivos, diretórios e ambiente do sistema.
import datetime
# Manipula datas e horas.
import subprocess
# Executa comandos shell externos.
import re
# Expressões regulares para extrair informações da saída do ping

# Arquivo de hosts de destinos
ARQUIVO_DESTINOS = os.path.join(os.environ["HOME"], "rede", "lista_destinos.txt")

# Diretório de log
DIRETORIO_LOG = os.path.join(os.environ["HOME"], "rede", "logs")

DATA_ATUAL = datetime.datetime.now().strftime("%d-%m-%Y")

# Arquivo de log
ARQUIVO_LOG = os.path.join(DIRETORIO_LOG, f"latencia_{DATA_ATUAL}.log")

# Configurações
QTD_PACOTES = 10
# Quantidade de pacotes ICMP enviados por destino

INTERVALO = 1
# Intervalo (em segundos) entre cada pacote enviado

# Verifica arquivo
if not os.path.isfile(ARQUIVO_DESTINOS):
# Garante que o arquivo de entrada existe

    print(f"ERRO: Arquivo {ARQUIVO_DESTINOS} não encontrado.")
    
    exit(1)
    # Sai do script

os.makedirs(DIRETORIO_LOG, exist_ok=True)
# Cria diretório se não existir

# Função estilo tee
def log_print(msg):
# Função para imprimir e salvar no log

    print(msg)
    with open(ARQUIVO_LOG, "a") as log:
    # Abre log em modo append

        log.write(msg + "\n")
        # Escreve mensagem no arquivo
        # Escreve no arquivo de log (sem sobrescrever)

log_print("==================================================")
log_print(" MONITORAMENTO DE LATÊNCIA E PERDA DE PACOTES")
log_print(f" Data: {datetime.datetime.now()}")
log_print("==================================================\n")

# Leitura dos destinos
with open(ARQUIVO_DESTINOS, "r") as arquivo:
# Abre arquivo com lista de destinos

    for linha in arquivo:
    # Itera linha por linha

        DESTINO = linha.strip()
        # Remove espaços e quebras de linha

        # Ignora linhas inválidas
        if not DESTINO or DESTINO.startswith("#"):
        # Evita linhas vazias ou comentários

            continue
            # Pula para próximo destino

        log_print(f"Destino: {DESTINO}")
        # Registra destino atual

        # Executa ping capturando saída
        resultado = subprocess.run(

            ["ping", "-c", str(QTD_PACOTES), "-i", str(INTERVALO), DESTINO],
            # -c = quantidade de pacotes | -i = intervalo entre pacotes

            stdout=subprocess.PIPE,
            # Captura saída padrão para análise

            stderr=subprocess.DEVNULL,
            # Ignora erros do comando

            text=True
            # Retorna saída como string (não bytes)
        )

        SAIDA_PING = resultado.stdout
        # Armazena saída do ping

        # Se não houve saída → falha
        if not SAIDA_PING:
        # Pode indicar host inacessível ou erro grave

            log_print("  Falha: destino inacessível\n")
            continue

        # =========================
        # Extração da perda (%)
        # =========================
        match_perda = re.search(r'(\d+)% packet loss', SAIDA_PING)
        # Busca padrão como "10% packet loss" usando regex

        PERDA = match_perda.group(1) if match_perda else "N/A"
        # Extrai o número da perda ou define como N/A se não encontrado

        # =========================
        # Extração da latência média
        # =========================
        LAT_MEDIA = "N/A"
        # Valor padrão caso não consiga extrair

        for linha_saida in SAIDA_PING.splitlines():
        # Percorre cada linha da saída do ping

            if "rtt" in linha_saida or "round-trip" in linha_saida:
            # Identifica linha que contém estatísticas de latência

                partes = linha_saida.split("=")[-1].strip().split("/")
                # Divide a linha para extrair min/avg/max/mdev

                if len(partes) >= 2:
                # Garante que existe valor de média

                    LAT_MEDIA = partes[1].strip()
                    # Segunda posição geralmente é a média

                break
                # Para após encontrar a linha correta

        log_print(f"  Perda de pacotes : {PERDA}%")
        # Exibe percentual de perda
        log_print(f"  Latência média   : {LAT_MEDIA} ms")
        # Exibe latência média em ms
        log_print("--------------------------------------------------")

print("\nMonitoramento concluído.")
print(f"Log salvo em: {ARQUIVO_LOG}")
