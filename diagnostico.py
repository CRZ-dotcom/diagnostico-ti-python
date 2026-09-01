import os
import platform
import socket
import psutil

def coletar_informacoes():
    print("=== COLETANDO DADOS DO SISTEMA ===")
    
    # 1. Informações do Sistema Operacional
    sistema = platform.system()
    versao = platform.release()
    arquitetura = platform.machine()
    
    # 2. Informações do Processador e Memória
    processador = platform.processor()
    memoria_total = round(psutil.virtual_memory().total / (1024**3), 2)
    
    # 3. Informações do Disco Principal
    disco_uso = psutil.disk_usage('/')
    disco_total = round(disco_uso.total / (1024**3), 2)
    disco_livre = round(disco_uso.free / (1024**3), 2)
    
    # 4. Informações de Rede
    nome_host = socket.gethostname()
    try:
        ip_local = socket.gethostbyname(nome_host)
    except Exception:
        ip_local = "Não identificado"
        
    # 5. Teste de Conexão com a Internet
    print("Testando conexão com a internet...")
    resposta_ping = os.system("ping -c 1 8.8.8.8" if platform.system() != "Windows" else "ping -n 1 8.8.8.8 > nul")
    status_internet = "Conectado" if resposta_ping == 0 else "Sem Conexão"

    # Montando o relatório de texto
    relatorio = f"""
==================================================
RELATÓRIO DE DIAGNÓSTICO DE MÁQUINA
==================================================
Nome do Computador: {nome_host}
Sistema Operacional: {sistema} {versao} ({arquitetura})
Processador: {processador}
Memória RAM Total: {memoria_total} GB

Armazenamento (C:):
  - Total: {disco_total} GB
  - Livre: {disco_livre} GB

Rede e Conectividade:
  - Endereço IP Local: {ip_local}
  - Status da Internet: {status_internet}
==================================================
    """
    
    # Exibe no terminal
    print(relatorio)
    
    # Salva em um arquivo .txt
    with open("relatorio_maquina.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(relatorio)
        
    print("Relatório salvo com sucesso em 'relatorio_maquina.txt'!")

if __name__ == "__main__":
    coletar_informacoes()