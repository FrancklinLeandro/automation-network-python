# automation-network-python

## Objetivo do Repositório

Este repositório contém **scripts Python** voltados para automação em **Infraestrutura de Redes**.

O foco é:

- Diagnóstico de conectividade
- Auditoria básica de segurança
- Monitoramento de dispositivos
- Automatização de tarefas repetitivas em ambientes Linux

Os scripts são desenvolvidos para uso prático em **laboratórios e ambientes corporativos**.

---

## Tipos de Automações

Este repositório inclui automações como:

- Verificação de portas TCP
- Testes de conectividade (ping, nc)
- Coleta de informações de rede
- Monitoramento de interfaces
- Scripts auxiliares para troubleshooting
- Diagnóstico de rota (traceroute) para múltiplos destinos com geração automática de log diário
- Auditoria de inventário de switches (comparação entre NetBox e planilha CSV)

Cada script contém **documentação detalhada no próprio código**, incluindo:

- objetivo
- requisitos
- exemplo de uso

---

## Scripts Disponíveis

Atualmente o repositório possui **2 scripts**, incluindo:

- switch-csv.py
- ap-scan.py

---

## Dependências

Algumas automações podem exigir:

- python3
- bibliotecas padrão do Python (ex: shutil, subprocess, os)
