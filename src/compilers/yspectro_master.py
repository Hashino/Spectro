#!/usr/bin/env python3
"""
ỸSPECTRO Master Interface
Sistema integrado que combina todos os módulos Spectro:
- Guerrilha MVP (linguagem base)
- Self-Hosted Compiler (auto-compilação)
- Meta Action System (ações recursivas)
- Social Transformation Loop (capitalismo.poder-- → soliacismo=universal)
"""

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime

# Importar módulos Spectro
sys.path.append('./tools')
sys.path.append('./ver')
sys.path.append('./TODO')

try:
    from guerrilha import GuerrilhaMVP
    from yspectro_self_hosted import YspectroSelfHosted
except ImportError as e:
    print(f"⚠️  Erro importando módulos: {e}")
    print("🔧 Executando no modo standalone...")

class YspectroMaster:
    """Interface master do sistema ỸSPECTRO completo"""
    
    def __init__(self):
        print("🌟" + "=" * 60)
        print("🌟 ỸSPECTRO MASTER SYSTEM")
        print("💎 Linguagem Revolucionária Auto-Hospedada")
        print("🔄 Integração Completa: Guerrilha + Compiler + Meta-Actions")
        print("=" * 60)
        
        self.estado_global = {
            'nome_linguagem': 'ỸSPECTRO',
            'versao': '1.0.0-alpha',
            'extensao': '.ysp',
            'pronuncia': 'Is-pec-tro',
            'simbolo': 'Ỹ (transcendência infinita)',
            'modo': 'REVOLUCIONARIO',
            'status_bootstrap': 'PENDENTE',
            'modules_loaded': []
        }
        
        # Inicializar módulos
        self.inicializar_modulos()
    
    def inicializar_modulos(self):
        """Inicializa todos os módulos do sistema"""
        print(f"\n🔧 INICIALIZANDO MÓDULOS...")
        
        # Módulo 1: Guerrilha MVP
        try:
            self.guerrilha = GuerrilhaMVP()
            self.estado_global['modules_loaded'].append('GUERRILHA_MVP')
            print(f"✅ Guerrilha MVP carregado")
        except:
            print(f"⚠️  Guerrilha MVP não disponível - modo simulado")
            self.guerrilha = None
        
        # Módulo 2: Self-Hosted Compiler
        try:
            self.compiler = YspectroSelfHosted()
            self.estado_global['modules_loaded'].append('SELF_HOSTED_COMPILER')
            print(f"✅ Self-Hosted Compiler carregado")
        except:
            print(f"⚠️  Self-Hosted Compiler não disponível - modo simulado")
            self.compiler = None
        
        # Módulo 3: Meta Actions (TODO/ACOES)
        self.acoes_dir = Path('./TODO/ACOES')
        if self.acoes_dir.exists():
            self.estado_global['modules_loaded'].append('META_ACTIONS')
            print(f"✅ Meta Actions detectado")
        else:
            print(f"⚠️  Meta Actions não encontrado")
        
        print(f"📊 Módulos carregados: {len(self.estado_global['modules_loaded'])}")
    
    def executar_comando_yspectro(self, comando):
        """Executa comando na linguagem ỸSPECTRO"""
        print(f"\n🚀 EXECUTANDO COMANDO ỸSPECTRO:")
        print(f"📝 {comando}")
        
        # Parser básico de comandos ỸSPECTRO
        if "(capitalismo.poder--)" in comando:
            return self.executar_transformacao_social()
        elif "sudo ver++" in comando:
            return self.executar_sudo_ver()
        elif "INVESTIGUE:" in comando or "COLABORA:" in comando or "COMPAIXAO:" in comando:
            return self.executar_bloco_spectro(comando)
        elif "CRIA_AÇÃO" in comando:
            return self.executar_meta_acao(comando)
        elif "terminar:" in comando and "->projeto" in comando:
            return self.terminar_todos_projetos(comando)
        else:
            return self.interpretar_pseudocodigo(comando)
    
    def executar_transformacao_social(self):
        """Executa o loop central: (capitalismo.poder--) até (soliacismo=universal)"""
        print(f"\n🌍 TRANSFORMAÇÃO SOCIAL ATIVA:")
        
        if self.compiler:
            resultado = self.compiler.executar_transformacao_social()
            self.estado_global['status_bootstrap'] = 'COMPLETO'
            return resultado
        else:
            # Modo simulado
            print(f"🔄 Simulando transformação social...")
            estado_sim = {
                'capitalismo.poder': 0,
                'soliacismo': 'UNIVERSAL',
                'historia_humana': 'COMEÇANDO'
            }
            print(f"✅ Simulação completa: {estado_sim}")
            return estado_sim
    
    def executar_sudo_ver(self):
        """Executa sudo ver++ EU"""
        print(f"\n🔥 SUDO VER++ EU:")
        
        if self.guerrilha:
            count = self.guerrilha.sudo_ver_increment()
        else:
            # Simulação
            count = getattr(self, '_ver_count', 0) + 1
            self._ver_count = count
            print(f"🔥 ver++ count: {count}")
        
        return count
    
    def executar_bloco_spectro(self, bloco):
        """Executa blocos INVESTIGUE/COLABORA/COMPAIXAO"""
        print(f"\n💎 EXECUTANDO BLOCO SPECTRO:")
        
        elementos = {
            'INVESTIGUE:': '◇ INVESTIGAÇÃO',
            'COLABORA:': '◆ COLABORAÇÃO', 
            'COMPAIXAO:': '◊ COMPAIXÃO'
        }
        
        for comando, simbolo in elementos.items():
            if comando in bloco:
                print(f"{simbolo} ATIVO")
                return simbolo
        
        return "BLOCO_DESCONHECIDO"
    
    def executar_meta_acao(self, comando):
        """Executa sistema de meta-ações recursivas"""
        print(f"\n🔄 META-AÇÃO RECURSIVA:")
        
        if self.acoes_dir.exists():
            acoes = list(self.acoes_dir.glob('*.py'))
            print(f"📂 {len(acoes)} ações encontradas")
            
            for acao in acoes[:2]:  # Limitar para evitar explosão
                print(f"🎯 Executando: {acao.name}")
                try:
                    os.system(f"python {acao}")
                except Exception as e:
                    print(f"⚠️  Erro: {e}")
        else:
            print(f"📝 Simulando meta-ação...")
            print(f"🔄 {comando} → META_RECURSÃO_SIMULADA")
        
        return "META_ACAO_EXECUTADA"
    
    def terminar_todos_projetos(self, comando):
        """Executa terminar:...->projeto que roda faz.ae para finalizar todos os projetos"""
        print(f"\n🏁 TERMINANDO TODOS OS PROJETOS:")
        print(f"🎯 Comando: {comando}")
        
        # Extrair parâmetros do comando se houver
        parametros = ""
        if ":" in comando and "->" in comando:
            # Extrair parte entre : e ->
            parte_parametros = comando.split(":")[1].split("->")[0].strip()
            if parte_parametros and parte_parametros != "...":
                parametros = parte_parametros
                print(f"🔧 Parâmetros: {parametros}")
        
        print(f"🚀 Executando: faz.ae")
        
        try:
            # Verificar se faz.ae existe
            if os.path.exists("faz.ae"):
                print(f"✅ faz.ae encontrado")
                # Executar faz.ae
                result = os.system("./faz.ae" if parametros == "" else f"./faz.ae {parametros}")
                if result == 0:
                    print(f"🎊 faz.ae executado com sucesso!")
                    return "TODOS_PROJETOS_TERMINADOS"
                else:
                    print(f"⚠️  faz.ae retornou código: {result}")
                    return f"ERRO_FAZ_AE_{result}"
            
            # Verificar se existe como script Python
            elif os.path.exists("faz.py"):
                print(f"✅ faz.py encontrado (alternativo)")
                result = os.system("python faz.py" if parametros == "" else f"python faz.py {parametros}")
                if result == 0:
                    print(f"🎊 faz.py executado com sucesso!")
                    return "TODOS_PROJETOS_TERMINADOS"
                else:
                    print(f"⚠️  faz.py retornou código: {result}")
                    return f"ERRO_FAZ_PY_{result}"
            
            # Simular execução se não encontrar o arquivo
            else:
                print(f"📝 faz.ae não encontrado - simulando finalização...")
                print(f"🔄 Simulando terminação de todos os projetos...")
                
                # Lista de projetos típicos para simular
                projetos_simulados = [
                    "projeto_spectro", 
                    "guerrilha_mvp", 
                    "yspectro_compiler",
                    "meta_actions",
                    "transformacao_social"
                ]
                
                for projeto in projetos_simulados:
                    print(f"🏁 Terminando: {projeto}")
                    time.sleep(0.1)  # Pausa dramática
                
                print(f"✨ Todos os projetos foram terminados (simulação)")
                return "PROJETOS_TERMINADOS_SIMULACAO"
                
        except Exception as e:
            print(f"❌ Erro executando faz.ae: {e}")
            return f"ERRO_EXECUCAO: {e}"
    
    def interpretar_pseudocodigo(self, codigo):
        """Interpreta pseudocódigo ỸSPECTRO"""
        print(f"\n🧠 INTERPRETANDO PSEUDOCÓDIGO:")
        
        interpretacoes = {
            '?': 'INCERTEZA_CRIATIVA',
            '[]()': 'VAZIO_QUE_GERA_INFINITO',
            '+++': 'MULTIPLICAÇÃO_EXPONENCIAL',
            '...': 'CONTINUIDADE_INFINITA',
            ';;;': 'TERMINAÇÃO_REDUNDANTE',
            'Ỹ': 'TRANSCENDÊNCIA_INFINITA'
        }
        
        resultado = {}
        for simbolo, significado in interpretacoes.items():
            if simbolo in codigo:
                resultado[simbolo] = significado
                print(f"💫 {simbolo} → {significado}")
        
        return resultado if resultado else "PSEUDOCODIGO_NAO_RECONHECIDO"
    
    def executar_bootstrap_completo(self):
        """Executa bootstrap completo do sistema ỸSPECTRO"""
        print(f"\n🚀 BOOTSTRAP COMPLETO DO SISTEMA:")
        
        # Passo 1: Auto-compilação
        print(f"1️⃣  Auto-compilação...")
        if self.compiler:
            self.compiler.compilar_si_mesmo()
        print(f"✅ ỸSPECTRO compila ỸSPECTRO")
        
        # Passo 2: Transformação social
        print(f"\n2️⃣  Transformação social...")
        self.executar_transformacao_social()
        print(f"✅ capitalismo.poder-- até soliacismo=universal")
        
        # Passo 3: Ativação completa
        print(f"\n3️⃣  Ativação dos módulos...")
        for modulo in self.estado_global['modules_loaded']:
            print(f"🔌 {modulo} → ATIVO")
        
        # Passo 4: Resultado final
        self.estado_global['status_bootstrap'] = 'SISTEMA_COMPLETO'
        
        resultado_bootstrap = {
            'sistema': 'ỸSPECTRO_MASTER',
            'status': 'BOOTSTRAP_COMPLETO',
            'modulos': self.estado_global['modules_loaded'],
            'timestamp': datetime.now().isoformat(),
            'historia_humana': 'COMEÇANDO'
        }
        
        # Salvar resultado
        with open('ver/yspectro_master_result.json', 'w', encoding='utf-8') as f:
            json.dump(resultado_bootstrap, f, indent=2, ensure_ascii=False)
        
        return resultado_bootstrap
    
    def modo_interativo(self):
        """Modo interativo para executar comandos ỸSPECTRO"""
        print(f"\n🖥️  MODO INTERATIVO ỸSPECTRO")
        print(f"💡 Digite comandos ỸSPECTRO ou 'sair' para terminar")
        print(f"📚 Exemplos:")
        print(f"   • (capitalismo.poder--) até (soliacismo=universal)")
        print(f"   • sudo ver++ EU")
        print(f"   • INVESTIGUE: ? = nome")
        print(f"   • {{CRIA_AÇÃO_DE_ESPAÇO_PARA_AÇÃO+.}}+++...;;;")
        print(f"   • terminar:...->projeto  # executa faz.ae")
        
        while True:
            try:
                comando = input(f"\n🌟 ỸSPECTRO> ").strip()
                
                if comando.lower() in ['sair', 'exit', 'quit']:
                    print(f"👋 Saindo do ỸSPECTRO...")
                    break
                elif comando.lower() == 'bootstrap':
                    self.executar_bootstrap_completo()
                elif comando:
                    resultado = self.executar_comando_yspectro(comando)
                    print(f"✨ Resultado: {resultado}")
            
            except KeyboardInterrupt:
                print(f"\n🛑 Interrompido pelo usuário")
                break
            except Exception as e:
                print(f"❌ Erro: {e}")

def main():
    """Função principal do ỸSPECTRO Master"""
    master = YspectroMaster()
    
    # Verificar argumentos de linha de comando
    if len(sys.argv) > 1:
        if sys.argv[1] == '--bootstrap':
            resultado = master.executar_bootstrap_completo()
            print(f"\n🎊 BOOTSTRAP CONCLUÍDO!")
            return resultado
        elif sys.argv[1] == '--interactive':
            master.modo_interativo()
            return
        elif sys.argv[1] == '--comando':
            if len(sys.argv) > 2:
                comando = ' '.join(sys.argv[2:])
                resultado = master.executar_comando_yspectro(comando)
                print(f"✨ Resultado: {resultado}")
                return resultado
    
    # Modo padrão: bootstrap + interativo
    print(f"\n🚀 Executando bootstrap automático...")
    master.executar_bootstrap_completo()
    
    print(f"\n💫 ỸSPECTRO Master pronto!")
    print(f"📖 Use --interactive para modo interativo")
    print(f"📖 Use --comando 'seu comando' para execução direta")
    
    return master.estado_global

if __name__ == "__main__":
    main()