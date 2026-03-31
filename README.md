# automation-network-python

## Objetivo do Repositório

Este repositório contém **scripts Python** voltados para automação em **Infraestrutura de Redes** — equivalentes funcionais das automações Bash, porém com **maior robustez, organização de código e escalabilidade** para ambientes maiores.

O foco é:
- Diagnóstico de conectividade
- Auditoria básica de segurança
- Monitoramento de dispositivos
- Automatização de tarefas repetitivas em ambientes Linux

Os scripts são desenvolvidos para uso prático em **laboratórios e ambientes corporativos**.

---

## Por que Python em vez de Bash?

As automações deste repositório cobrem as mesmas tarefas presentes em scripts Bash, com vantagens concretas:

| Aspecto | Bash | Python |
|---|---|---|
| Tratamento de erros | Limitado | Robusto (`try/except`) |
| Organização do código | Linear | Modular e reutilizável |
| Escalabilidade | Difícil | Fácil de expandir |
| Geração de relatórios | Manual | Automatizada e estruturada |
| Manutenção | Frágil | Clara e documentada |

---

## Tipos de Automações

- Verificação de portas TCP
- Testes de conectividade (ping, nc)
- Coleta de informações de rede
- Monitoramento de interfaces
- Scripts auxiliares para troubleshooting
- Diagnóstico de rota (traceroute) com geração automática de log diário
- Auditoria de inventário de switches (comparação entre NetBox e planilha CSV)

Cada script contém **documentação detalhada no próprio código**, incluindo objetivo, requisitos e exemplo de uso.

---

## Scripts

### switch-csv.py

Realiza **teste de conectividade (ping) em múltiplos switches** listados em arquivos CSV, classificando cada dispositivo como **UP ou DOWN** e gerando **relatório consolidado em log**.
```bash
./switch-csv.py
```

### ap-scan.py

Realiza **verificação de conectividade de Access Points (APs)** via ICMP (`ping`), lendo uma lista estruturada de dispositivos e registrando **status UP/DOWN em log diário**.
```bash
./ap-scan.py
```

### TCP-port-checker.py
Realiza **verificação de portas TCP em múltiplos hosts**, utilizando sockets nativos, com **log persistente e tratamento de erros de rede/DNS**.
```bash
./TCP-port-checker.py
```

### host-monitor.py
Realiza **monitoramento de conectividade (ping em lote)**, com execução via `subprocess`, log persistente e contagem de hosts UP/DOWN.
```bash
./host-monitor.py
```

## Estrutura do Repositório
```
automation-network-python/
├── connectivity/
│   ├── TCP-port-checker.py
│   ├── ap-scan.py
│   ├── host-monitor.py
│   └── switch-csv.py
├── NOTA.md
└── README.md
```
