#!/usr/bin/env python3
"""
Interpretação de ? = `mover` [valor] ./TODO/
Operação de movimentação de valor para diretório TODO
"""

import os
import json
import shutil
from datetime import datetime
from pathlib import Path

def mover_valor_para_todo(valor_origem, destino_todo="./TODO/"):
    """
    ? = `mover` [valor] ./TODO/
    
    Interpretação:
    - ? = resultado da operação de movimento
    - `mover` = comando/operação de transferência  
    - [valor] = valor/conteúdo a ser movido
    - ./TODO/ = diretório de destino
    """
    
    # Criar diretório TODO se não existir
    todo_path = Path(destino_todo)
    todo_path.mkdir(exist_ok=True)
    
    # Metadados da operação de movimento
    movimento = {
        'timestamp': datetime.now().isoformat(),
        'operacao': 'mover',
        'valor_origem': valor_origem,
        'destino': str(todo_path.absolute()),
        'status': 'processando'
    }
    
    print(f"🚀 Executando: ? = `mover` [valor] ./TODO/")
    print(f"📦 Valor a mover: {valor_origem}")
    print(f"📁 Destino: {destino_todo}")
    
    # Diferentes tipos de movimento baseado no tipo do valor
    if isinstance(valor_origem, dict):
        # Mover dados estruturados
        arquivo_destino = todo_path / f"valor_movido_{datetime.now().strftime('%H%M%S')}.json"
        with open(arquivo_destino, 'w', encoding='utf-8') as f:
            json.dump(valor_origem, f, indent=2, ensure_ascii=False)
        movimento['arquivo_criado'] = str(arquivo_destino)
        movimento['tipo'] = 'dados_estruturados'
        
    elif isinstance(valor_origem, str) and os.path.exists(valor_origem):
        # Mover arquivo existente
        arquivo_origem = Path(valor_origem)
        arquivo_destino = todo_path / arquivo_origem.name
        shutil.copy2(arquivo_origem, arquivo_destino)
        movimento['arquivo_criado'] = str(arquivo_destino)
        movimento['tipo'] = 'arquivo'
        
    elif isinstance(valor_origem, str):
        # Mover string como texto
        arquivo_destino = todo_path / f"texto_movido_{datetime.now().strftime('%H%M%S')}.txt"
        with open(arquivo_destino, 'w', encoding='utf-8') as f:
            f.write(valor_origem)
        movimento['arquivo_criado'] = str(arquivo_destino)
        movimento['tipo'] = 'texto'
        
    else:
        # Mover valor genérico
        arquivo_destino = todo_path / f"valor_{datetime.now().strftime('%H%M%S')}.txt"
        with open(arquivo_destino, 'w', encoding='utf-8') as f:
            f.write(str(valor_origem))
        movimento['arquivo_criado'] = str(arquivo_destino)
        movimento['tipo'] = 'generico'
    
    movimento['status'] = 'concluido'
    
    # Log da operação
    log_path = todo_path / "movimentos.log"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{json.dumps(movimento, ensure_ascii=False)}\n")
    
    print(f"✅ Movimento concluído: {movimento['arquivo_criado']}")
    print(f"📋 Log: {log_path}")
    
    # O resultado da operação ? =
    resultado = {
        'operacao_concluida': True,
        'valor_movido': movimento['arquivo_criado'],
        'timestamp': movimento['timestamp'],
        'tipo_movimento': movimento['tipo']
    }
    
    return resultado

# Testes das diferentes interpretações do movimento
print("🌟 ? = `mover` [valor] ./TODO/")
print()

# Teste 1: Mover dados dos cálculos anteriores
valores_spectro = {
    'todos_valor': 'VALOR_COLETIVO_INCREMENTAL',
    'complexidade': 'REDUÇÃO_GRADUAL_DISTRIBUÍDA', 
    'transcendencia': 'PROCESSO_CONTÍNUO',
    'elementos': ['◇', '◈', '◆', '◊']
}

resultado1 = mover_valor_para_todo(valores_spectro)
print(f"📊 Resultado 1: {resultado1['tipo_movimento']}")
print()

# Teste 2: Mover texto conceitual
texto_conceito = """
◇ INVESTIGAÇÃO: ? representa potencial infinito
◈ APRENDIZAGEM: mover é transformar
◆ COLABORAÇÃO: [valor] se distribui no ./TODO/
◊ COMPAIXÃO: o movimento cria espaço para novos valores
"""

resultado2 = mover_valor_para_todo(texto_conceito)
print(f"📊 Resultado 2: {resultado2['tipo_movimento']}")
print()

print("💫 Interpretação Spectro:")
print("◇ ? = RESULTADO_DO_MOVIMENTO")
print("◈ `mover` = OPERAÇÃO_DE_TRANSFORMAÇÃO")
print("◆ [valor] = CONTEÚDO_A_SER_REDISTRIBUÍDO") 
print("◊ ./TODO/ = ESPAÇO_DE_POTENCIAL_FUTURO")
print()
print("🎯 ? = CRIAÇÃO_DE_ESPAÇO_PARA_AÇÃO")
print("   Mover valor para TODO significa preparar para execução futura")