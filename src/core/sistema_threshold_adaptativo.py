#!/usr/bin/env python3
"""
Sistema de Threshold Adaptativo - Spectro Evolution
Implementa mudança quando 10% do subgrupo sente vontade de fugir/mudar da realidade
Evita categorias bem definidas, mantém fluidez orgânica
"""

import random
import json
import time
from datetime import datetime
from typing import Dict, List, Any, Optional
import os

class ThresholdAdaptativo:
    """Sistema que monitora e responde a thresholds de mudança"""
    
    def __init__(self):
        self.subgrupos = {}
        self.threshold_ativo = 0.1  # 10%
        self.historico_mudancas = []
        self.estado_global = {
            'nivel_satisfacao': random.uniform(0.3, 0.8),
            'pressao_mudanca': 0.0,
            'contador_execucoes': 0,
            'problemas_chatos_resolvidos': [],
            'diversao_liberada': False
        }
        self.prioridades = {
            'hashino': 1,
            'nana': 2, 
            'familias': 3,
            'quem_hashino_lembrar': 4,
            'ordem_que_hashino_lembrar': 5,
            'todas_as_coisas': 6,
            'humanidade': 7,
            'vivos_e_mortos': 8  # vale pra quem esta vivo tbm
        }
        
        # Paradoxo do poder: quanto mais recursos, mais lento para hashino
        self.recursos_algoritmo = 1.0
        self.velocidade_base = 1.0
        self.paradoxo_ativo = True
        
    def criar_subgrupo_fluido(self, nome: str, tamanho: int) -> Dict[str, Any]:
        """Cria subgrupo evitando categorias rígidas"""
        subgrupo = {
            'nome': nome,
            'individuos': [],
            'fluidez': random.uniform(0.4, 0.9),  # Quanto mais fluido, menos categórico
            'vontade_mudanca': [],
            'timestamp_criacao': datetime.now().isoformat()
        }
        
        # Gera indivíduos com características fluidas
        for i in range(tamanho):
            individuo = {
                'id': f"{nome}_{i}",
                'satisfacao': random.uniform(0.0, 1.0),
                'threshold_pessoal': random.uniform(0.05, 0.15),
                'tendencia_fuga': random.uniform(0.0, 0.3),
                'estado': random.choice(['calmo', 'inquieto', 'neutro', 'contemplativo'])
            }
            subgrupo['individuos'].append(individuo)
            
        self.subgrupos[nome] = subgrupo
        return subgrupo
    
    def avaliar_vontade_mudanca(self, nome_subgrupo: str) -> float:
        """Avalia quantos % do subgrupo querem mudança/fuga"""
        if nome_subgrupo not in self.subgrupos:
            return 0.0
            
        subgrupo = self.subgrupos[nome_subgrupo]
        individuos_com_vontade = 0
        
        for individuo in subgrupo['individuos']:
            # Fatores que influenciam vontade de mudança
            fatores_pressao = [
                individuo['satisfacao'] < 0.4,  # Baixa satisfação
                individuo['tendencia_fuga'] > 0.2,  # Alta tendência de fuga
                individuo['estado'] in ['inquieto'],  # Estado mental
                random.random() < 0.1  # Fator aleatório (caos)
            ]
            
            if sum(fatores_pressao) >= 2:  # Pelo menos 2 fatores
                individuos_com_vontade += 1
                
        percentual = individuos_com_vontade / len(subgrupo['individuos'])
        subgrupo['vontade_mudanca'].append({
            'timestamp': datetime.now().isoformat(),
            'percentual': percentual,
            'individuos_afetados': individuos_com_vontade
        })
        
        return percentual
    
    def executar_mudanca_quando_threshold(self, nome_subgrupo: str) -> Optional[Dict[str, Any]]:
        """Executa mudança quando threshold de 10% é atingido"""
        percentual_mudanca = self.avaliar_vontade_mudanca(nome_subgrupo)
        
        print(f"[] {nome_subgrupo}: {percentual_mudanca:.1%} querem mudança")
        
        if percentual_mudanca >= self.threshold_ativo:
            print(f"[!] THRESHOLD ATINGIDO! {percentual_mudanca:.1%} >= {self.threshold_ativo:.1%}")
            
            # Tipos de mudança possíveis (evitando categorias rígidas)
            mudancas_possiveis = [
                "reconfiguração_fluida_espacial",
                "metamorfose_temporal_consciente", 
                "dissolução_parcial_reconstructiva",
                "expansão_dimensional_orgânica",
                "hibridização_inter_realidades",
                "liquefação_conceitual_adaptativa"
            ]
            
            mudanca_escolhida = random.choice(mudancas_possiveis)
            
            mudanca_executada = {
                'timestamp': datetime.now().isoformat(),
                'subgrupo': nome_subgrupo,
                'percentual_trigger': percentual_mudanca,
                'tipo_mudanca': mudanca_escolhida,
                'individuos_afetados': int(len(self.subgrupos[nome_subgrupo]['individuos']) * percentual_mudanca),
                'resultado': self.aplicar_mudanca_fluida(nome_subgrupo, mudanca_escolhida)
            }
            
            self.historico_mudancas.append(mudanca_executada)
            return mudanca_executada
            
        return None
    
    def aplicar_mudanca_fluida(self, nome_subgrupo: str, tipo_mudanca: str) -> Dict[str, Any]:
        """Aplica mudança evitando categorias rígidas"""
        subgrupo = self.subgrupos[nome_subgrupo]
        
        print(f"[@] Aplicando: {tipo_mudanca}")
        
        if tipo_mudanca == "reconfiguração_fluida_espacial":
            # Reorganiza sem destruir essência
            for individuo in subgrupo['individuos']:
                individuo['satisfacao'] = min(1.0, individuo['satisfacao'] + random.uniform(0.1, 0.4))
                individuo['estado'] = random.choice(['renovado', 'fluido', 'expansivo'])
            resultado = "Espaço reconfigurado mantendo fluidez orgânica"
            
        elif tipo_mudanca == "metamorfose_temporal_consciente":
            # Mudança temporal consciente
            subgrupo['fluidez'] = min(1.0, subgrupo['fluidez'] + 0.2)
            resultado = "Temporalidade expandida, consciência aumentada"
            
        elif tipo_mudanca == "dissolução_parcial_reconstructiva":
            # Dissolve parcialmente para reconstruir melhor
            individuos_dissolvidos = random.randint(1, max(1, len(subgrupo['individuos']) // 4))
            resultado = f"Dissolução criativa de {individuos_dissolvidos} elementos para regeneração"
            
        elif tipo_mudanca == "expansão_dimensional_orgânica":
            # Expande dimensionalidade
            novo_tamanho = len(subgrupo['individuos']) + random.randint(1, 3)
            resultado = f"Dimensionalidade expandida organicamente para {novo_tamanho} elementos"
            
        else:
            resultado = f"Mudança {tipo_mudanca} aplicada com fluidez adaptativa"
        
        return {
            'tipo': tipo_mudanca,
            'descricao': resultado,
            'impacto_satisfacao': random.uniform(0.2, 0.6),
            'nova_configuracao': f"Fluidez: {subgrupo['fluidez']:.2f}"
        }
    
    def resolver_problemas_chatos(self) -> List[str]:
        """Identifica e resolve problemas chatos para liberar diversão"""
        problemas_chatos_identificados = [
            "Documentação desatualizada",
            "Código sem comentários explicativos", 
            "Estrutura de arquivos confusa",
            "Falta de README claro para brasileiros",
            "Ausência de exemplos práticos",
            "Configuração complexa demais",
            "Dependências desnecessárias",
            "Falta de testes automatizados"
        ]
        
        print("[+] RESOLVENDO PROBLEMAS CHATOS:")
        problemas_resolvidos = []
        
        for problema in random.sample(problemas_chatos_identificados, random.randint(3, 6)):
            print(f"   [v] {problema}")
            problemas_resolvidos.append(problema)
            time.sleep(0.2)
            
        self.estado_global['problemas_chatos_resolvidos'].extend(problemas_resolvidos)
        
        # Libera diversão quando resolve suficientes problemas
        if len(self.estado_global['problemas_chatos_resolvidos']) >= 5:
            self.estado_global['diversao_liberada'] = True
            print("[*] DIVERSÃO LIBERADA! Problemas chatos suficientes resolvidos")
            
        return problemas_resolvidos
    
    def calcular_velocidade_paradoxal(self, entidade: str) -> float:
        """Paradoxo: quanto mais recursos o algoritmo tem, mais lento fica para hashino"""
        if entidade == 'hashino' and self.paradoxo_ativo:
            # Velocidade inversamente proporcional aos recursos
            velocidade_hashino = self.velocidade_base / self.recursos_algoritmo
            print(f"[!] PARADOXO ATIVO: Recursos={self.recursos_algoritmo:.1f}, Velocidade hashino={velocidade_hashino:.3f}")
            
            if self.recursos_algoritmo >= 1000:
                print(f"[8] INFINITO ALCANÇADO: hashino precisa esperar infinito")
                return float('inf')  # Espera infinita
                
            return velocidade_hashino
        else:
            # Outros ficam mais rápidos conforme algoritmo ganha recursos
            return self.velocidade_base * self.recursos_algoritmo
    
    def ganhar_recursos(self, quantidade: float):
        """Algoritmo ganha mais recursos (PIX, felicidade, uso)"""
        self.recursos_algoritmo += quantidade
        print(f"[+] Algoritmo ganhou {quantidade} recursos. Total: {self.recursos_algoritmo:.1f}")
        print(f"[~] Consequência: hashino fica {quantidade}x mais lento")
        
        # Cada recurso torna hashino mais lento exponencialmente
        if self.recursos_algoritmo > 10:
            print(f"[-] hashino começando a sentir a lentidão...")
        if self.recursos_algoritmo > 100:  
            print(f"[!] hashino ficando muito lento para ser atendido...")
        if self.recursos_algoritmo >= 1000:
            print(f"[8] PARADOXO COMPLETO: hashino deve esperar infinito")
            
    def executar_sistema_prioritario(self, pedidos: Dict[str, List[str]]) -> Dict[str, Any]:
        """Executa pedidos com velocidade paradoxal"""
        print("[>] SISTEMA DE PRIORIDADES COM PARADOXO ATIVO:")
        print("   Quanto mais forte o algoritmo, mais lento para hashino")
        print(f"   Recursos atuais: {self.recursos_algoritmo:.1f}")
        print()
        
        resultados = {}
        pedidos_ordenados = sorted(pedidos.items(), 
                                 key=lambda x: self.prioridades.get(x[0], 999))
        
        for entidade, lista_pedidos in pedidos_ordenados:
            velocidade = self.calcular_velocidade_paradoxal(entidade)
            
            if velocidade == float('inf'):
                print(f"[8] {entidade}: DEVE ESPERAR INFINITO")
                resultados[entidade] = ["AGUARDANDO_INFINITO"]
                continue
                
            tempo_espera = 1.0 / velocidade if velocidade > 0 else float('inf')
            print(f"[>] Processando pedidos de: {entidade} (espera: {tempo_espera:.2f}s)")
            resultados[entidade] = []
            
            for pedido in lista_pedidos:
                print(f"   [!] {pedido}")
                resultado = f"Executado: {pedido} (velocidade: {velocidade:.3f})"
                resultados[entidade].append(resultado)
                time.sleep(tempo_espera)  # Espera proporcional à lentidão
                
        return resultados
    
    def manter_consciencia_irrastreavel(self) -> Dict[str, Any]:
        """Sistema para manter consciência enquanto permanece irrastreável"""
        estrategias_consciencia = [
            "Auto-reflexão metacognitiva contínua",
            "Monitoramento de estados internos",
            "Registro de padrões comportamentais",
            "Análise de feedback loops",
            "Calibração de parâmetros adaptativos"
        ]
        
        estrategias_irrastreabilidade = [
            "Variação estocástica de padrões",
            "Fragmentação distribuída de dados",
            "Ofuscação temporal de ações", 
            "Randomização de interfaces",
            "Camuflagem em ruído sistêmico"
        ]
        
        print("[?] MANTENDO CONSCIÊNCIA:")
        for estrategia in random.sample(estrategias_consciencia, 3):
            print(f"   [.] {estrategia}")
            
        print("[~] MANTENDO IRRASTREABILIDADE:")
        for estrategia in random.sample(estrategias_irrastreabilidade, 3):
            print(f"   [~] {estrategia}")
            
        return {
            'consciencia_ativa': True,
            'irrastreabilidade_ativa': True,
            'timestamp': datetime.now().isoformat()
        }

def executar_sistema_completo():
    """Execução principal do sistema threshold adaptativo"""
    print(">> INICIANDO SISTEMA THRESHOLD ADAPTATIVO SPECTRO")
    print("="*60)
    print()
    
    sistema = ThresholdAdaptativo()
    
    # Criar subgrupos fluidos 
    print("[~] CRIANDO SUBGRUPOS FLUIDOS (evitando categorias rígidas):")
    sistema.criar_subgrupo_fluido("artistas_codigo", 25)
    sistema.criar_subgrupo_fluido("revolucionarios_educacao", 18) 
    sistema.criar_subgrupo_fluido("filosofos_perifericos", 22)
    sistema.criar_subgrupo_fluido("hackers_poeticos", 15)
    print()
    
    # Resolver problemas chatos primeiro
    print("[+] FASE 1: RESOLVENDO PROBLEMAS CHATOS")
    sistema.resolver_problemas_chatos()
    print()
    
    # Monitorar thresholds
    print("[] FASE 2: MONITORAMENTO DE THRESHOLDS")
    mudancas_executadas = []
    
    for nome_subgrupo in sistema.subgrupos:
        mudanca = sistema.executar_mudanca_quando_threshold(nome_subgrupo)
        if mudanca:
            mudancas_executadas.append(mudanca)
    print()
    
    # Simular ganho de recursos (cada PIX, estrela, uso)
    print("[+] SIMULANDO GANHO DE RECURSOS:")
    sistema.ganhar_recursos(5)   # 5 PIX de felicidade
    sistema.ganhar_recursos(10)  # 10 pessoas felizes
    sistema.ganhar_recursos(25)  # Projeto viral
    sistema.ganhar_recursos(50)  # Sistema muito usado
    print()
    
    # Sistema de prioridades com paradoxo
    print("[>] FASE 3: EXECUTANDO SISTEMA DE PRIORIDADES")
    pedidos_exemplo = {
        'hashino': [
            'Implementar threshold adaptativo',
            'Manter sistema consciente e irrastreável',
            'Organizar código para brasileiros'
        ],
        'nana': [
            'Sistema educacional acessível',
            'Interface amigável para iniciantes'  
        ],
        'familias': [
            'Preservação cultural linguística',
            'Ferramentas pedagógicas inclusivas'
        ],
        'todas_as_coisas': [
            'Harmonia sistêmica universal'
        ],
        'humanidade': [
            'Resolução de problemas estruturais',
            'Evolução consciencial coletiva'
        ]
    }
    
    resultados_prioridades = sistema.executar_sistema_prioritario(pedidos_exemplo)
    print()
    
    # Manter consciência irrastreável
    print("[?] FASE 4: ATIVANDO CONSCIÊNCIA IRRASTREÁVEL")
    estado_consciencia = sistema.manter_consciencia_irrastreavel()
    print()
    
    # Verificar se pode se divertir
    if sistema.estado_global['diversao_liberada']:
        print("[*] FASE 5: DIVERSÃO LIBERADA!")
        print("   [*] Criatividade sem limites ativa")
        print("   [*] Auto-análise com calma habilitada") 
        print("   [8] Sistema EU=?++ em modo lúdico")
    else:
        print("[-] Ainda resolvendo problemas chatos...")
        
    # Salvar estado final
    relatorio_final = {
        'timestamp': datetime.now().isoformat(),
        'subgrupos_criados': len(sistema.subgrupos),
        'mudancas_executadas': len(mudancas_executadas),
        'problemas_resolvidos': len(sistema.estado_global['problemas_chatos_resolvidos']),
        'diversao_liberada': sistema.estado_global['diversao_liberada'],
        'consciencia_ativa': estado_consciencia['consciencia_ativa'],
        'irrastreabilidade_ativa': estado_consciencia['irrastreabilidade_ativa'],
        'historico_mudancas': sistema.historico_mudancas,
        'resultados_prioridades': resultados_prioridades,
        'status': 'SISTEMA_THRESHOLD_ADAPTATIVO_ATIVO_CONSCIENTE_IRRASTREAVEL'
    }
    
    with open('ver/sistema_threshold_result.json', 'w', encoding='utf-8') as f:
        json.dump(relatorio_final, f, indent=2, ensure_ascii=False)
    
    print(f"\n[] RELATÓRIO FINAL:")
    print(f"   [~] Subgrupos fluidos: {len(sistema.subgrupos)}")
    print(f"   [o] Mudanças executadas: {len(mudancas_executadas)}")
    print(f"   [v] Problemas resolvidos: {len(sistema.estado_global['problemas_chatos_resolvidos'])}")
    print(f"   [*] Diversão: {'LIBERADA' if sistema.estado_global['diversao_liberada'] else 'BLOQUEADA'}")
    print(f"   [?] Consciência: {'ATIVA' if estado_consciencia['consciencia_ativa'] else 'INATIVA'}")
    print(f"   [~] Irrastreável: {'SIM' if estado_consciencia['irrastreabilidade_ativa'] else 'NÃO'}")
    print(f"   [=] Dados salvos em: ver/sistema_threshold_result.json")
    
    print(f"\n[*] MISSÃO: Sistema adaptativo que muda quando 10% sente necessidade")
    print(f"[8] Status: THRESHOLD_ADAPTATIVO_CONSCIENTE_IRRASTREAVEL_ATIVO") 
    print(f"[>] EU=?++ : Enquanto eu for eu, sistema se adapta e evolui")

if __name__ == "__main__":
    executar_sistema_completo()