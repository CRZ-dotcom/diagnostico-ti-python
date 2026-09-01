# 🛠️ Diagnóstico e Inventário de TI em Python

> Ferramenta em Python desenvolvida para automação de rotinas de diagnóstico, inventário de hardware e checagem de conectividade para **Suporte Técnico e Helpdesk (Nível 1/2)**.

---

## 📌 Sobre o Projeto

Este script foi criado para otimizar o atendimento de suporte técnico, permitindo a coleta rápida e automatizada de dados essenciais da estação de trabalho do usuário e gerando um relatório consolidado em texto para análise rápida.

---

## ⚙️ Funcionalidades

- **Sistema Operacional:** Leitura do SO, versão e arquitetura do hardware.
- **Métricas de Hardware:** Mapeamento em tempo real do uso de Memória RAM e Espaço em Disco (Total e Livre).
- **Rede Local:** Identificação do IP Local e Nome do Host na rede.
- **Teste de Conectividade:** Teste dinâmico de comunicação com a internet via ICMP Ping.
- **Relatório Automático:** Exportação de todas as métricas coletadas para um arquivo `.txt`.

---

## 🛠️ Tecnologias Utilizadas

- **[Python 3](https://www.python.org/):** Linguagem principal do projeto.
- **[psutil](https://pypi.org/project/psutil/):** Biblioteca para leitura de métricas do sistema e hardware.
- **Módulos Nativos:** `os`, `platform`, `socket`.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o **Python 3** instalado em sua máquina.

### Passo a Passo

1. **Instale a biblioteca necessária no terminal:**
```bash
pip install psutil
Execute o script:

Bash
python diagnostico.py
Verifique o resultado:
O relatório detalhado será exibido diretamente no terminal e salvo no arquivo relatorio_maquina.txt na mesma pasta do projeto.

📝 Licença
Este projeto foi desenvolvido para fins educacionais e de portfólio.
