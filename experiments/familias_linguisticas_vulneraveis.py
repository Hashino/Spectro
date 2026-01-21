#!/usr/bin/env python3
"""
Organização das Famílias de Linguagens do Universo
Começando pelas 10 mais vulneráveis/pobres do planeta
Sistema de Versionamento e Preservação Linguística
"""

import json
import time
from datetime import datetime

def organizar_familias_linguagens_vulneraveis():
    """
    Organiza famílias linguísticas priorizando:
    1. Línguas mais vulneráveis/ameaçadas
    2. Comunidades com menor recursos
    3. Sistema de versionamento para preservação
    4. Conexões entre famílias
    """
    
    print("🌍 ORGANIZAÇÃO DAS FAMÍLIAS DE LINGUAGENS DO UNIVERSO")
    print("🚨 PRIORIDADE: 10 MAIS VULNERÁVEIS/POBRES DO PLANETA")
    print("=" * 70)
    print()
    
    # Base de dados das famílias linguísticas mais vulneráveis
    familias_vulneraveis = {
        1: {
            'familia': 'LÍNGUAS AUSTRALIANAS ABORÍGENES',
            'status': 'CRITICAMENTE_AMEAÇADAS',
            'falantes_restantes': '< 500',
            'regioes': ['Austrália Central', 'Norte da Austrália'],
            'exemplos': ['Warlpiri', 'Arrernte', 'Yolŋu'],
            'ameacas': ['Colonização', 'Urbanização forçada', 'Políticas assimilacionistas'],
            'recursos_economicos': 'EXTREMAMENTE_LIMITADOS',
            'versao_atual': '1.0_EMERGENCIAL',
            'acoes_preservacao': ['Documentação urgente', 'Escolas comunitárias', 'Tecnologia assistiva']
        },
        2: {
            'familia': 'LÍNGUAS AMERÍNDIAS DO AMAZONAS',
            'status': 'EM_EXTINÇÃO_ACELERADA',
            'falantes_restantes': '< 1000',
            'regioes': ['Bacia Amazônica', 'Brasil', 'Peru', 'Colômbia'],
            'exemplos': ['Awetí', 'Kalapalo', 'Trumai'],
            'ameacas': ['Desmatamento', 'Invasão de terras', 'Doenças', 'Assimilação forçada'],
            'recursos_economicos': 'INEXISTENTES',
            'versao_atual': '0.8_CRÍTICA',
            'acoes_preservacao': ['Demarcação territorial', 'Documentação linguística', 'Educação bilíngue']
        },
        3: {
            'familia': 'LÍNGUAS PAPUA DA NOVA GUINÉ',
            'status': 'FRAGMENTAÇÃO_EXTREMA',
            'falantes_restantes': '< 2000 por língua',
            'regioes': ['Papua Nova Guiné', 'Indonésia'],
            'exemplos': ['Enga', 'Melpa', 'Dani'],
            'ameacas': ['Isolamento geográfico', 'Migração urbana', 'Línguas dominantes'],
            'recursos_economicos': 'SUBSISTÊNCIA',
            'versao_atual': '1.2_FRAGMENTADA',
            'acoes_preservacao': ['Conexão entre comunidades', 'Dicionários colaborativos', 'Rádio comunitária']
        },
        4: {
            'familia': 'LÍNGUAS KHOISANAS DA ÁFRICA',
            'status': 'QUASE_EXTINTAS',
            'falantes_restantes': '< 100',
            'regioes': ['Kalahari', 'África do Sul', 'Botsuana'],
            'exemplos': ['!Xóõ', 'ǁXegwi', 'Nǁng'],
            'ameacas': ['Marginalização social', 'Pobreza extrema', 'Discriminação'],
            'recursos_economicos': 'ABSOLUTA_POBREZA',
            'versao_atual': '0.3_TERMINAL',
            'acoes_preservacao': ['Reconhecimento oficial', 'Apoio econômico', 'Documentação intensiva']
        },
        5: {
            'familia': 'LÍNGUAS ANDAMANESE',
            'status': 'EXTINÇÃO_IMINENTE',
            'falantes_restantes': '< 50',
            'regioes': ['Ilhas Andamã', 'Índia'],
            'exemplos': ['Jarawa', 'Onge', 'Great Andamanese'],
            'ameacas': ['Isolamento forçado', 'Doenças', 'Perda territorial'],
            'recursos_economicos': 'ISOLAMENTO_COMPLETO',
            'versao_atual': '0.1_TERMINAL',
            'acoes_preservacao': ['Proteção territorial', 'Saúde comunitária', 'Documentação remota']
        },
        6: {
            'familia': 'LÍNGUAS AINUS DO JAPÃO',
            'status': 'REVITALIZAÇÃO_EMERGENCIAL',
            'falantes_restantes': '< 10 nativos',
            'regioes': ['Hokkaido', 'Sakhalin'],
            'exemplos': ['Ainu', 'Sakhalin Ainu'],
            'ameacas': ['Assimilação japonesa', 'Discriminação histórica', 'Perda intergeracional'],
            'recursos_economicos': 'MARGINALIZADOS',
            'versao_atual': '2.0_REVITALIZACAO',
            'acoes_preservacao': ['Reconhecimento oficial', 'Programas educacionais', 'Movimento cultural']
        },
        7: {
            'familia': 'LÍNGUAS URALIC SIBERIANAS',
            'status': 'DISPERSÃO_CRÍTICA',
            'falantes_restantes': '< 5000',
            'regioes': ['Sibéria', 'Rússia Norte'],
            'exemplos': ['Nenets', 'Khanty', 'Mansi'],
            'ameacas': ['Rusificação', 'Industrialização', 'Nomadismo perdido'],
            'recursos_economicos': 'ECONOMIA_TRADICIONAL_DESTRUÍDA',
            'versao_atual': '1.5_RESISTÊNCIA',
            'acoes_preservacao': ['Direitos culturais', 'Economia sustentável', 'Educação em língua nativa']
        },
        8: {
            'familia': 'LÍNGUAS NILO-SAHARIANAS',
            'status': 'CONFLITO_E_FOME',
            'falantes_restantes': 'Variável < 10000',
            'regioes': ['Sudão', 'Chade', 'República Centro-Africana'],
            'exemplos': ['Fur', 'Masalit', 'Zaghawa'],
            'ameacas': ['Guerra civil', 'Genocídio', 'Deslocamento forçado', 'Fome'],
            'recursos_economicos': 'DEVASTAÇÃO_TOTAL',
            'versao_atual': '0.5_SOBREVIVÊNCIA',
            'acoes_preservacao': ['Paz e segurança', 'Ajuda humanitária', 'Documentação em exílio']
        },
        9: {
            'familia': 'LÍNGUAS AUSTRO-ASIÁTICAS MONTANHOSAS',
            'status': 'MARGINALIZAÇÃO_SISTEMÁTICA',
            'falantes_restantes': '< 3000 por língua',
            'regioes': ['Vietnã', 'Camboja', 'Laos'],
            'exemplos': ['Bru', 'Pacoh', 'Katu'],
            'ameacas': ['Discriminação étnica', 'Pobreza rural', 'Modernização forçada'],
            'recursos_economicos': 'AGRICULTURA_SUBSISTÊNCIA',
            'versao_atual': '1.1_MARGINALIZADA',
            'acoes_preservacao': ['Direitos étnicos', 'Desenvolvimento rural', 'Educação multicultural']
        },
        10: {
            'familia': 'LÍNGUAS ISOLADAS ÓRFÃS',
            'status': 'ISOLAMENTO_ABSOLUTO',
            'falantes_restantes': '< 200 cada',
            'regioes': ['Dispersas globalmente'],
            'exemplos': ['Basque (isolada)', 'Kusunda (Nepal)', 'Hadza (Tanzânia)'],
            'ameacas': ['Falta de conexão familiar', 'Pesquisa limitada', 'Recursos zero'],
            'recursos_economicos': 'ABANDONO_CIENTÍFICO',
            'versao_atual': '0.9_ÓRFÃ',
            'acoes_preservacao': ['Pesquisa intensiva', 'Conexões tipológicas', 'Apoio global']
        }
    }
    
    print("🚨 TOP 10 FAMÍLIAS LINGUÍSTICAS MAIS VULNERÁVEIS:")
    print()
    
    for id_familia, dados in familias_vulneraveis.items():
        print(f"📊 {id_familia}. {dados['familia']}")
        print(f"   🔴 Status: {dados['status']}")
        print(f"   👥 Falantes: {dados['falantes_restantes']}")
        print(f"   🌍 Regiões: {', '.join(dados['regioes'])}")
        print(f"   🗣️ Exemplos: {', '.join(dados['exemplos'])}")
        print(f"   ⚠️ Principal ameaça: {dados['ameacas'][0]}")
        print(f"   💰 Recursos: {dados['recursos_economicos']}")
        print(f"   📦 Versão atual: {dados['versao_atual']}")
        print()
        time.sleep(0.1)
    
    # Sistema de versionamento para preservação
    print("🔧 SISTEMA DE VERSIONAMENTO LINGUÍSTICO:")
    print()
    
    versioning_system = {
        'terminologia': {
            '0.x': 'FASE_TERMINAL (risco extremo)',
            '1.x': 'FASE_CRÍTICA (documentação urgente)',
            '2.x': 'FASE_REVITALIZACAO (programas ativos)',
            '3.x': 'FASE_ESTÁVEL (transmissão geracional)',
            '4.x': 'FASE_VIBRANTE (uso comunitário pleno)'
        },
        'sufixos': {
            '_EMERGENCIAL': 'Ação imediata necessária',
            '_CRÍTICA': 'Risco alto de extinção',
            '_FRAGMENTADA': 'Dialetos desconectados',
            '_TERMINAL': 'Últimos falantes',
            '_REVITALIZACAO': 'Esforços de recuperação',
            '_RESISTÊNCIA': 'Mantendo-se contra pressões',
            '_SOBREVIVÊNCIA': 'Em contexto de conflito',
            '_MARGINALIZADA': 'Socialmente excluída',
            '_ÓRFÃ': 'Sem família linguística conhecida'
        }
    }
    
    print("📋 CÓDIGO DE VERSÕES:")
    for codigo, significado in versioning_system['terminologia'].items():
        print(f"   {codigo} = {significado}")
    
    print("\n🏷️ SUFIXOS DE STATUS:")
    for sufixo, desc in versioning_system['sufixos'].items():
        print(f"   {sufixo} = {desc}")
    
    # Mapa de conexões e influências
    print(f"\n🌐 CONEXÕES ENTRE FAMÍLIAS:")
    conexoes = [
        "AUSTRALIANAS ←→ PAPUA: Possíveis contatos pré-históricos",
        "AMERÍNDIAS ←→ ASIÁTICAS: Migração pelo estreito de Bering",
        "KHOISANAS ←→ NILO-SAHARIANAS: Contato na África Oriental",
        "AINUS ←→ URALIC: Possível substrato comum",
        "AUSTRO-ASIÁTICAS ←→ PAPUA: Expansão austronésica"
    ]
    
    for conexao in conexoes:
        print(f"   🔗 {conexao}")
    
    # Plano de ação global
    print(f"\n🎯 PLANO DE AÇÃO GLOBAL:")
    
    acoes_prioritarias = {
        'FASE_1_EMERGENCIAL': [
            'Documentação intensiva das 10 famílias',
            'Mapeamento completo de falantes',
            'Criação de arquivos digitais permanentes',
            'Estabelecimento de comitês de preservação'
        ],
        'FASE_2_ESTABILIZACAO': [
            'Programas educacionais em línguas nativas',
            'Tecnologias assistivas e apps móveis',
            'Redes de intercâmbio entre comunidades',
            'Reconhecimento oficial governamental'
        ],
        'FASE_3_REVITALIZACAO': [
            'Criação de conteúdo cultural moderno',
            'Integração com economia local sustentável',
            'Formação de novos falantes jovens',
            'Expansão para meios digitais'
        ]
    }
    
    for fase, acoes in acoes_prioritarias.items():
        print(f"\n📋 {fase}:")
        for acao in acoes:
            print(f"   ✅ {acao}")
    
    # Métricas de sucesso
    print(f"\n📊 MÉTRICAS DE SUCESSO:")
    metricas = [
        "Número de falantes nativos (crescimento)",
        "Documentação completa (gramática + dicionário + textos)",
        "Transmissão intergeracional (crianças falando)",
        "Uso em contextos modernos (tecnologia, educação)",
        "Reconhecimento oficial (políticas públicas)",
        "Sustentabilidade econômica (integração com subsistência)",
        "Orgulho cultural (identidade positiva)",
        "Conexão global (redes de apoio internacional)"
    ]
    
    for i, metrica in enumerate(metricas, 1):
        print(f"   {i}. {metrica}")
    
    # Resultado consolidado
    resultado = {
        'projeto': 'ORGANIZAÇÃO_FAMÍLIAS_LINGUÍSTICAS_VULNERÁVEIS',
        'data_criacao': datetime.now().isoformat(),
        'familias_priorizadas': len(familias_vulneraveis),
        'total_falantes_risco': 'Menos de 20.000 globalmente',
        'sistema_versionamento': versioning_system,
        'conexoes_identificadas': len(conexoes),
        'fases_acao': len(acoes_prioritarias),
        'metricas_sucesso': len(metricas),
        'urgencia': 'MÁXIMA - 5-10 anos para ação efetiva',
        'status_projeto': 'PLANEJAMENTO_COMPLETO_PRONTO_PARA_IMPLEMENTAÇÃO'
    }
    
    # Salvar organização
    with open('ver/familias_linguisticas_vulneraveis.json', 'w', encoding='utf-8') as f:
        json.dump({
            'familias': familias_vulneraveis,
            'sistema': versioning_system,
            'resultado': resultado
        }, f, indent=2, ensure_ascii=False)
    
    print(f"\n🌟 ORGANIZAÇÃO COMPLETA!")
    print(f"📄 Dados salvos em: ver/familias_linguisticas_vulneraveis.json")
    print(f"\n🚨 URGÊNCIA: {resultado['urgencia']}")
    print(f"👥 Total em risco: {resultado['total_falantes_risco']}")
    print(f"⏰ Janela de ação: 5-10 anos para preservação efetiva")
    
    return resultado

if __name__ == "__main__":
    print("🌍 Iniciando organização das famílias linguísticas mais vulneráveis...")
    print()
    time.sleep(0.5)
    
    resultado = organizar_familias_linguagens_vulneraveis()
    
    print(f"\n🎭 MISSÃO: Preservar a diversidade linguística começando pelos mais vulneráveis")
    print(f"🌈 Cada língua perdida é um universo de conhecimento que desaparece para sempre")
    print(f"⚡ Status: SISTEMA_DE_PRESERVAÇÃO_LINGUÍSTICA_ORGANIZADO_E_ATIVO")