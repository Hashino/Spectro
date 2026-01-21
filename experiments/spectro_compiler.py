#!/usr/bin/env python3
"""
Spectro Ver++ Compiler MVP
Compilador experimental para linguagem de guerrilha programática Spectro
Inspirado na filosofia de transformação através da arte e código
"""

import os
import sys
import json
import hashlib
import datetime
import subprocess
import re
from pathlib import Path
from typing import Dict, List, Any, Optional

class SpectroCompiler:
    """Compilador MVP para linguagem Spectro com elementos experimentais"""
    
    def __init__(self, build_dir: str = "./ver"):
        self.build_dir = Path(build_dir)
        self.build_dir.mkdir(exist_ok=True)
        
        # Estado do compilador
        self.version_count = 0
        self.compile_context = {}
        self.output_artifacts = []
        
        # Linguagens de referência suportadas
        self.supported_langs = {
            'rust': {'ext': '.rs', 'cmd': 'rustc'},
            'lua': {'ext': '.lua', 'cmd': 'lua'},
            'c': {'ext': '.c', 'cmd': 'gcc'},
            'fish': {'ext': '.fish', 'cmd': 'fish'},
            'python': {'ext': '.py', 'cmd': 'python3'}
        }
        
        # Tokens da linguagem guerrilha
        self.tokens = {
            'sudo ver++': 'VERSION_INCREMENT',
            'EU': 'SELF',
            'MEUS_PARÇA': 'PARTNERS', 
            'NOSSAS_FAMILIAS': 'FAMILIES',
            'UNIVERSO': 'UNIVERSE',
            'O ROLE': 'EXECUTE_SESSION',
            'final.': 'TERMINATE',
            'enquanto': 'WHILE_LOOP',
            'manda um pix': 'TRANSFER_REQUEST',
            '!PAIS': 'NOT_COUNTRY',
            'INVESTIGUE:': 'INVESTIGATE_BLOCK',
            'COLABORA:': 'COLLABORATE_BLOCK',
            'COMPAIXAO:': 'COMPASSION_BLOCK',
            'PERGUNTA INICIAL:': 'INITIAL_QUESTION'
        }
        
        print(f"🚀 Spectro Ver++ Compiler MVP inicializado")
        print(f"📁 Diretório de build: {self.build_dir.absolute()}")
    
    def tokenize(self, source_code: str) -> List[Dict[str, Any]]:
        """Tokeniza código fonte da linguagem guerrilha"""
        tokens = []
        lines = source_code.strip().split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
                
            token_info = {
                'line': line_num,
                'content': line,
                'tokens': [],
                'type': 'UNKNOWN'
            }
            
            # Identifica tokens conhecidos
            for pattern, token_type in self.tokens.items():
                if pattern in line:
                    token_info['tokens'].append(token_type)
                    token_info['type'] = token_type
                    break
            
            tokens.append(token_info)
        
        return tokens
    
    def compile_to_python(self, tokens: List[Dict[str, Any]]) -> str:
        """Compila tokens para código Python executável com melhor tratamento de blocos"""
        python_code = []
        python_code.append("#!/usr/bin/env python3")
        python_code.append('"""')
        python_code.append("Código compilado da linguagem ỸSPECTRO")
        python_code.append(f"Compilado em: {datetime.datetime.now()}")
        python_code.append('"""')
        python_code.append("")
        python_code.append("import random")
        python_code.append("import time")
        python_code.append("import json")
        python_code.append("from datetime import datetime")
        python_code.append("")
        
        # Função principal que será chamada no final
        python_code.append("def executar_yspectro():")
        python_code.append("    \"\"\"Executa o programa ỸSPECTRO compilado\"\"\"")
        python_code.append("    # Estado da execução")
        python_code.append("    estado = {")
        python_code.append("        'ver_count': 0,")
        python_code.append("        'execucoes': [],")
        python_code.append("        'familias': ['arte', 'código', 'revolução', 'amor', 'liberdade'],")
        python_code.append("        'capitalismo.poder': 100,")
        python_code.append("        'soliacismo': 0,")
        python_code.append("        'historia_humana': 'PAUSADA'")
        python_code.append("    }")
        python_code.append("")
        
        # Traduz cada token para Python
        current_block = None
        inside_function = False
        function_indent = "    "
        
        for i, token in enumerate(tokens):
            if token['type'] == 'VERSION_INCREMENT':
                python_code.append(f"{function_indent}# sudo ver++ EU")
                python_code.append(f"{function_indent}estado['ver_count'] += 1")
                python_code.append(f"{function_indent}print(f'🔥 ver++ count: {{estado[\"ver_count\"]}}')")
                python_code.append("")
                
            elif token['type'] == 'EXECUTE_SESSION':
                python_code.append(f"{function_indent}# O ROLE!!!!!!!")
                python_code.append(f"{function_indent}print('🎯 O ROLE EXECUTANDO...')")
                python_code.append(f"{function_indent}print('📱 celular está no bolso')")
                python_code.append(f"{function_indent}print('💼 sessão de coworking anual ativa')")
                python_code.append(f"{function_indent}familia_selecionada = random.choice(estado['familias'])")
                python_code.append(f"{function_indent}print(f'👨‍👩‍👧‍👦 Família: {{familia_selecionada}}')")
                python_code.append(f"{function_indent}estado['execucoes'].append({{")
                python_code.append(f"{function_indent}    'timestamp': datetime.now().isoformat(),")
                python_code.append(f"{function_indent}    'familia': familia_selecionada")
                python_code.append(f"{function_indent}}})")
                python_code.append("")
                
            elif token['type'] == 'INITIAL_QUESTION':
                question = token['content'].replace('PERGUNTA INICIAL:', '').strip().strip('"')
                python_code.append(f"{function_indent}# PERGUNTA INICIAL")
                python_code.append(f"{function_indent}print('🤔 {question}')")
                python_code.append("")
                
            elif token['type'] == 'INVESTIGATE_BLOCK':
                python_code.append(f"{function_indent}# ◇ INVESTIGACAO")
                current_block = 'INVESTIGATE'
                
            elif token['type'] == 'COLLABORATE_BLOCK':
                python_code.append(f"{function_indent}# ◆ COLABORACAO") 
                current_block = 'COLLABORATE'
                
            elif token['type'] == 'COMPASSION_BLOCK':
                python_code.append(f"{function_indent}# ◊ COMPAIXAO")
                current_block = 'COMPASSION'
                
            elif token['type'] == 'TERMINATE':
                python_code.append(f"{function_indent}# ROLE TERMINOU")
                python_code.append(f"{function_indent}print('🎯 PROCESSO FINALIZADO')")
                python_code.append(f"{function_indent}return estado")
                python_code.append("")
                
            elif token['type'] == 'UNKNOWN' and current_block:
                line_content = token['content'].strip()
                
                if not line_content or line_content.startswith('#'):
                    continue
                    
                # Detectar definições de função
                if line_content.startswith('def ') or '():' in line_content:
                    python_code.append(f"{function_indent}{line_content}")
                    inside_function = True
                    function_indent = "        "
                    
                # Detectar blocos de controle
                elif any(line_content.startswith(kw) for kw in ['if ', 'elif ', 'else:', 'while ', 'for ']):
                    python_code.append(f"{function_indent}{line_content}")
                    
                # Detectar return statements
                elif line_content.startswith('return'):
                    python_code.append(f"{function_indent}{line_content}")
                    inside_function = False
                    function_indent = "    "
                    
                # Detectar chamadas de função e operações
                elif ('=' in line_content and not line_content.startswith('#')) or \
                     line_content.startswith('print(') or \
                     line_content.endswith('()') or \
                     any(op in line_content for op in ['+= ', '-= ', '*= ', '/=']):
                    python_code.append(f"{function_indent}{line_content}")
                    
                # Detectar comentários e descrições  
                elif line_content.startswith(('Como ', 'O ROLE', '->', 'núcleo_', 'Estado')):
                    python_code.append(f"{function_indent}# {line_content}")
                    
                # Código Python direto (começando com espaços significa que já está indentado)
                elif line_content.startswith('    '):
                    clean_line = line_content.strip()
                    python_code.append(f"{function_indent}{clean_line}")
                    
                # Qualquer outro código válido
                elif not line_content.startswith(('"', "'")):
                    python_code.append(f"{function_indent}{line_content}")
        
        # Finalizar função principal e adicionar chamada
        python_code.append("")
        python_code.append("if __name__ == '__main__':")
        python_code.append("    resultado_final = executar_yspectro()")
        python_code.append("    print('\\n🌟 ỸSPECTRO EXECUTADO COM SUCESSO!')")
        python_code.append("    print(f'   Estado final: {resultado_final}')")
        
        return '\n'.join(python_code)
    
    def compile_to_rust(self, tokens: List[Dict[str, Any]]) -> str:
        """Compila tokens para código Rust"""
        rust_code = []
        rust_code.append("// Código Spectro compilado para Rust")
        rust_code.append("use std::collections::HashMap;")
        rust_code.append("use std::time::{SystemTime, UNIX_EPOCH};")
        rust_code.append("")
        rust_code.append("fn main() {")
        rust_code.append('    println!("🚀 Spectro Rust MVP");')
        rust_code.append("    let mut ver_count = 0u32;")
        rust_code.append("")
        
        for token in tokens:
            if token['type'] == 'VERSION_INCREMENT':
                rust_code.append("    // sudo ver++ EU")
                rust_code.append("    ver_count += 1;")
                rust_code.append('    println!("🔥 ver++ count: {}", ver_count);')
                rust_code.append("")
                
            elif token['type'] == 'EXECUTE_SESSION':
                rust_code.append("    // O ROLE!!!!!!!")
                rust_code.append('    println!("🎯 O ROLE EXECUTANDO...");')
                rust_code.append('    println!("📱 celular está no bolso");')
                rust_code.append("")
                
            elif token['type'] == 'TERMINATE':
                rust_code.append("    // final.")
                rust_code.append('    println!("🎯 PROCESSO FINALIZADO");')
                rust_code.append('    println!("📊 Ver count: {}", ver_count);')
        
        rust_code.append("}")
        return '\n'.join(rust_code)
    
    def compile_to_c(self, tokens: List[Dict[str, Any]]) -> str:
        """Compila tokens para código C"""
        c_code = []
        c_code.append("// Código Spectro compilado para C")
        c_code.append("#include <stdio.h>")
        c_code.append("#include <stdlib.h>")
        c_code.append("")
        c_code.append("int main() {")
        c_code.append('    printf("🚀 Spectro C MVP\\n");')
        c_code.append("    int ver_count = 0;")
        c_code.append("")
        
        for token in tokens:
            if token['type'] == 'VERSION_INCREMENT':
                c_code.append("    // sudo ver++ EU")
                c_code.append("    ver_count++;")
                c_code.append('    printf("🔥 ver++ count: %d\\n", ver_count);')
                c_code.append("")
                
            elif token['type'] == 'EXECUTE_SESSION':
                c_code.append("    // O ROLE!!!!!!!")
                c_code.append('    printf("🎯 O ROLE EXECUTANDO...\\n");')
                c_code.append("")
                
            elif token['type'] == 'TERMINATE':
                c_code.append("    // final.")
                c_code.append('    printf("🎯 PROCESSO FINALIZADO\\n");')
        
        c_code.append("    return 0;")
        c_code.append("}")
        return '\n'.join(c_code)
    
    def compile_file(self, source_file: str, target_langs: Optional[List[str]] = None) -> Dict[str, str]:
        """Compila arquivo fonte para linguagens especificadas"""
        if target_langs is None:
            target_langs = ['python']
        
        source_path = Path(source_file)
        if not source_path.exists():
            raise FileNotFoundError(f"Arquivo fonte não encontrado: {source_file}")
        
        print(f"📖 Compilando: {source_path.name}")
        
        # Ler código fonte
        with open(source_path, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Tokenizar
        tokens = self.tokenize(source_code)
        print(f"🔤 Tokens encontrados: {len(tokens)}")
        
        # Compilar para cada linguagem alvo
        compiled_files = {}
        
        for lang in target_langs:
            if lang == 'python':
                compiled_code = self.compile_to_python(tokens)
                output_file = self.build_dir / f"{source_path.stem}_compiled.py"
            elif lang == 'rust':
                compiled_code = self.compile_to_rust(tokens)
                output_file = self.build_dir / f"{source_path.stem}_compiled.rs"
            elif lang == 'c':
                compiled_code = self.compile_to_c(tokens)
                output_file = self.build_dir / f"{source_path.stem}_compiled.c"
            else:
                print(f"⚠️  Linguagem {lang} não suportada ainda")
                continue
            
            # Escrever arquivo compilado
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(compiled_code)
            
            compiled_files[lang] = str(output_file)
            print(f"✅ {lang.upper()}: {output_file}")
        
        return compiled_files
    
    def execute_compiled(self, compiled_file: str, lang: str) -> bool:
        """Executa arquivo compilado"""
        try:
            if lang == 'python':
                result = subprocess.run(['python3', compiled_file], 
                                      capture_output=True, text=True, timeout=30)
            elif lang == 'rust':
                # Compilar primeiro
                exe_file = compiled_file.replace('.rs', '')
                compile_result = subprocess.run(['rustc', compiled_file, '-o', exe_file],
                                              capture_output=True, text=True)
                if compile_result.returncode != 0:
                    print(f"❌ Erro compilando Rust: {compile_result.stderr}")
                    return False
                result = subprocess.run([exe_file], capture_output=True, text=True, timeout=30)
            elif lang == 'c':
                # Compilar primeiro
                exe_file = compiled_file.replace('.c', '')
                compile_result = subprocess.run(['gcc', compiled_file, '-o', exe_file],
                                              capture_output=True, text=True)
                if compile_result.returncode != 0:
                    print(f"❌ Erro compilando C: {compile_result.stderr}")
                    return False
                result = subprocess.run([exe_file], capture_output=True, text=True, timeout=30)
            else:
                print(f"❌ Execução não suportada para {lang}")
                return False
            
            if result.returncode == 0:
                print(f"✅ Execução {lang} bem-sucedida:")
                print(result.stdout)
                return True
            else:
                print(f"❌ Erro na execução {lang}:")
                print(result.stderr)
                return False
                
        except subprocess.TimeoutExpired:
            print(f"⏱️  Timeout na execução de {compiled_file}")
            return False
        except Exception as e:
            print(f"❌ Erro executando {compiled_file}: {e}")
            return False
    
    def build_project(self, source_dir: str = ".", targets: Optional[List[str]] = None) -> Dict[str, Any]:
        """Build completo do projeto"""
        if targets is None:
            targets = ['python']
        
        print(f"🏗️  Iniciando build do projeto Spectro")
        
        # Procurar arquivos fonte
        source_files = []
        for ext in ['.spectro', '.guerrilha', '.sp']:
            source_files.extend(Path(source_dir).glob(f"**/*{ext}"))
        
        # Se não encontrar arquivos específicos, usar guerrilha.py como exemplo
        if not source_files:
            guerrilha_file = Path("tools/guerrilha.py")
            if guerrilha_file.exists():
                print("📄 Usando tools/guerrilha.py como fonte de exemplo")
                # Criar arquivo .spectro temporário com pseudocódigo
                temp_source = self.build_dir / "exemplo.spectro"
                with open(temp_source, 'w', encoding='utf-8') as f:
                    f.write("""# Exemplo Spectro - Linguagem de Guerrilha Programática
sudo ver++ EU; MEUS_PARÇA; NOSSAS_FAMILIAS(aleatoriamente); !PAIS; UNIVERSO EU=PROMPTER(conta ver);
enquanto você não conseguir manda um pix pro meu CPF kkkkk
O ROLE!!!!!!
sudo ver++ EU; MEUS_PARÇA;
final.
""")
                source_files = [temp_source]
        
        build_results = {
            'compiled_files': {},
            'executed_successfully': [],
            'errors': []
        }
        
        # Compilar cada arquivo fonte
        for source_file in source_files:
            try:
                compiled = self.compile_file(str(source_file), targets)
                build_results['compiled_files'][str(source_file)] = compiled
                
                # Executar arquivos compilados
                for lang, compiled_file in compiled.items():
                    if self.execute_compiled(compiled_file, lang):
                        build_results['executed_successfully'].append(compiled_file)
                        
            except Exception as e:
                error_msg = f"Erro compilando {source_file}: {e}"
                build_results['errors'].append(error_msg)
                print(f"❌ {error_msg}")
        
        # Salvar relatório de build
        build_report = self.build_dir / "build_report.json"
        with open(build_report, 'w', encoding='utf-8') as f:
            json.dump(build_results, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"📋 Relatório salvo em: {build_report}")
        return build_results

def main():
    """Função principal do compilador MVP"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Spectro Ver++ Compiler MVP")
    parser.add_argument('--source', '-s', help='Arquivo fonte para compilar')
    parser.add_argument('--targets', '-t', nargs='+', 
                       choices=['python', 'rust', 'c'], 
                       default=['python'],
                       help='Linguagens alvo para compilação')
    parser.add_argument('--build', '-b', action='store_true',
                       help='Build completo do projeto')
    parser.add_argument('--execute', '-e', action='store_true',
                       help='Executar arquivos compilados')
    
    args = parser.parse_args()
    
    compiler = SpectroCompiler()
    
    if args.build:
        results = compiler.build_project(targets=args.targets)
        print(f"\n🎯 Build concluído:")
        print(f"   ✅ Sucesso: {len(results['executed_successfully'])}")
        print(f"   ❌ Erros: {len(results['errors'])}")
    
    elif args.source:
        compiled_files = compiler.compile_file(args.source, args.targets)
        
        if args.execute:
            for lang, file_path in compiled_files.items():
                print(f"\n🚀 Executando {lang}:")
                compiler.execute_compiled(file_path, lang)
    
    else:
        print("Use --build para build completo ou --source para arquivo específico")
        print("Exemplo: python ver_compiler.py --build --targets python rust")

if __name__ == "__main__":
    main()