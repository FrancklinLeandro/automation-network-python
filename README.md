# 🚀 automation-network-python

## 🎯 Objetivo

Repositório de automação em **Python** voltado para **infraestrutura Linux, operações e redes**, com foco em scripts mais **robustos, escaláveis e estruturados** para ambientes reais.

Este projeto representa a evolução das automações em Bash, com foco em:

- Administração e monitoramento de infraestrutura Linux  
- Diagnóstico e troubleshooting de conectividade  
- Auditoria de segurança básica  
- Automação de tarefas operacionais  
- Geração de logs e relatórios estruturados  

---

## 🔥 Casos de Uso

Os scripts simulam atividades comuns em ambientes de:

- Infraestrutura Linux  
- NOC (Network Operations Center)  
- Operações de rede  
- Administração de sistemas  
- Auditoria e troubleshooting  

---

## 🆚 Bash vs Python

| Aspecto | Bash | Python |
|---|---|---|
| Tratamento de erros | Limitado | Robusto (`try/except`) |
| Organização do código | Linear | Modular e reutilizável |
| Escalabilidade | Difícil | Fácil de expandir |
| Logs e relatórios | Simples | Estruturados e automatizados |
| Manutenção | Frágil | Clara e sustentável |

---

## 🛠️ Tipos de Automação

- Verificação de portas TCP (sockets nativos)  
- Monitoramento de hosts e latência  
- Diagnóstico de rota (traceroute)  
- Coleta e análise de informações de sistema e rede  
- Automação de tarefas com logs persistentes  

Todos os scripts incluem:
- tratamento de erros  
- validação de entrada  
- geração de logs estruturados  

---

## 📂 Scripts

### 📡 switch-csv.py
Monitoramento de switches via **ping em lote (CSV)** com log consolidado

### 📶 ap-scan.py
Monitoramento de Access Points via ICMP

### 🔎 TCP-port-checker.py
Verificação de portas TCP com **sockets nativos e tratamento de erro**

### 🖥️ host-monitor.py
Monitoramento de conectividade com contagem de hosts **UP/DOWN**

### 📊 latency-monitor.py
Análise de latência e perda de pacotes com parsing via **regex**

### 🌐 traceroute.py
Diagnóstico de rota com execução via subprocess e log detalhado

---

## 🗂️ Estrutura
```
automation-network-python/
├── connectivity/
│   ├── TCP-port-checker.py
│   ├── ap-scan.py
│   ├── host-monitor.py
│   ├── latency-monitor.py
│   ├── switch-csv.py
│   └── traceroute.py
├── NOTA.md
└── README.md
```
---

## 🚀 Diferencial

- Automação estruturada para **infraestrutura Linux e administração de sistemas**  
- Código modular, escalável e reutilizável  
- Tratamento de erros robusto  
- Logs organizados para análise e troubleshooting  
- Foco em automação operacional de ambientes reais   
