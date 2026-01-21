#!/usr/bin/env python3
"""
Spectro Learning Session Reflection Tool

Uma ferramenta de linha de comando para ajudar educadores e aprendizes a refletir sobre 
sessões de aprendizagem baseadas em parceria usando os princípios da metodologia Spectro.
Versão aprimorada com análise de padrões e insights longitudinais.
"""

import datetime
import json
import os
import argparse
import statistics
import logging
from pathlib import Path
from collections import Counter, defaultdict

class SpectroReflection:
    def __init__(self):
        self.session_data = {}
        self.reflection_dir = Path.home() / ".spectro_reflections"
        self.reflection_dir.mkdir(exist_ok=True)
        
        # Setup logging
        self.log_dir = Path.home() / ".spectro_logs"
        self.log_dir.mkdir(exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(
                    self.log_dir / f"reflection_{datetime.date.today()}.log",
                    encoding='utf-8'
                ),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger("spectro.reflection")
        
        # Elementos fundamentais do Spectro
        self.elementos = {
            '◇': 'Compaixão Sem Limites',
            '◈': 'Centrado na Pergunta', 
            '◆': 'Dirigido pelo Aprendiz',
            '◊': 'Autocuidado Primeiro'
        }
    
    def gather_reflection(self):
        """Guia o usuário através do processo de reflexão baseado nos princípios Spectro"""
        print("=== Reflexão de Sessão de Aprendizagem Spectro ===\n")
        self.logger.info("🚀 Iniciando nova sessão de reflexão")
        
        # Informações básicas da sessão
        self.session_data['date'] = datetime.date.today().isoformat()
        self.session_data['participants'] = input("Quem participou desta parceria? ")
        self.session_data['context'] = input("Qual foi o contexto/assunto de aprendizagem? ")
        
        self.logger.info(f"📝 Sessão: {self.session_data['context']} com {self.session_data['participants']}")
        
        print("\n--- Reflexões dos Elementos Fundamentais ---")
        
        # Elemento ◈ - Nunca abandone a pergunta
        print("\n◈ Inquéritos que moveram a aprendizagem hoje:")
        questions = []
        while True:
            q = input("Digite um inquérito (ou pressione enter para continuar): ")
            if not q:
                break
            questions.append(q)
            self.logger.info(f"◈ INQUIRY: {q}")
        self.session_data['driving_inquiries'] = questions
        
        new_questions = []
        print("\nNovos inquéritos que emergiram:")
        while True:
            q = input("Digite um novo inquérito (ou pressione enter para continuar): ")
            if not q:
                break
            new_questions.append(q)
            self.logger.info(f"◈ NEW_INQUIRY: {q}")
        self.session_data['new_inquiries'] = new_questions
        
        # Elemento ◆ - Aprendiz dirige a aprendizagem
        self.session_data['learner_agency'] = input(
            "\n◆ Como o aprendiz exerceu autonomia/direção hoje? "
        )
        if self.session_data['learner_agency']:
            self.logger.info(f"◆ LEARNER_AGENCY: {self.session_data['learner_agency']}")
        
        # Elemento ◇ - Compaixão sem limites
        self.session_data['compassion_expressions'] = input(
            "\n◇ Como a compaixão/cuidado foi expressa nesta sessão? "
        )
        if self.session_data['compassion_expressions']:
            self.logger.info(f"◇ COMPASSION: {self.session_data['compassion_expressions']}")
        
        # Elemento ◊ - Autocuidado em primeiro lugar
        self.session_data['self_preservation'] = input(
            "\n◊ Como você praticou autocuidado durante esta sessão? "
        )
        if self.session_data['self_preservation']:
            self.logger.info(f"◊ SELF_CARE: {self.session_data['self_preservation']}")
        
        # Reflexões gerais
        print("\n--- Reflexão Geral ---")
        self.session_data['flourished'] = input("O que floresceu hoje? ")
        self.session_data['challenges'] = input("O que se mostrou desafiador? ")
        self.session_data['insights'] = input("Que insights surgiram? ")
        self.session_data['next_steps'] = input("Quais são os possíveis próximos passos? ")
        
        if self.session_data['insights']:
            self.logger.info(f"💡 INSIGHT: {self.session_data['insights']}")
        if self.session_data['challenges']:
            self.logger.info(f"🌱 CHALLENGE: {self.session_data['challenges']}")
        
        
    def save_reflection(self):
        """Salva reflexão em arquivo JSON"""
        filename = f"reflection_{self.session_data['date']}.json"
        filepath = self.reflection_dir / filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.session_data, f, indent=2, ensure_ascii=False)
            
            self.logger.info(f"✅ Reflexão salva: {filepath}")
            print(f"\n✓ Reflexão salva em: {filepath}")
            
        except Exception as e:
            self.logger.error(f"❌ Erro ao salvar reflexão: {e}")
            print(f"❌ Erro ao salvar: {e}")
    
    
    def view_recent_reflections(self, days=7):
        """Exibe reflexões recentes"""
        print(f"\n=== Reflexões Recentes (últimos {days} dias) ===")
        
        cutoff_date = datetime.date.today() - datetime.timedelta(days=days)
        reflection_files = list(self.reflection_dir.glob("reflection_*.json"))
        
        recent_reflections = []
        for file in reflection_files:
            try:
                date_str = file.stem.split('_')[1]
                file_date = datetime.date.fromisoformat(date_str)
                if file_date >= cutoff_date:
                    recent_reflections.append((file_date, file))
            except (ValueError, IndexError):
                continue
        
        recent_reflections.sort(reverse=True)
        
        if not recent_reflections:
            print("Nenhuma reflexão recente encontrada.")
            return
        
        for date, file in recent_reflections:
            with open(file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"\n--- {date} ---")
            print(f"Participantes: {data.get('participants', 'N/A')}")
            print(f"Contexto: {data.get('context', 'N/A')}")
            print(f"Inquéritos Principais: {', '.join(data.get('driving_inquiries', []))}")
            if data.get('insights'):
                print(f"Insights: {data['insights']}")
    
    def analyze_patterns(self, days=30):
        """Analisa padrões longitudinais nas reflexões"""
        print(f"\n=== Análise de Padrões ({days} dias) ===")
        
        cutoff_date = datetime.date.today() - datetime.timedelta(days=days)
        reflection_files = list(self.reflection_dir.glob("reflection_*.json"))
        
        reflections = []
        for file in reflection_files:
            try:
                date_str = file.stem.split('_')[1]
                file_date = datetime.date.fromisoformat(date_str)
                if file_date >= cutoff_date:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    data['file_date'] = file_date
                    reflections.append(data)
            except (ValueError, IndexError, json.JSONDecodeError):
                continue
        
        if not reflections:
            print("Dados insuficientes para análise de padrões.")
            return
        
        # Análise de frequência de elementos Spectro
        print("\n📊 Engajamento com Elementos Fundamentais:")
        elementos_presentes = defaultdict(int)
        
        for reflection in reflections:
            if reflection.get('learner_agency'):
                elementos_presentes['◆ Dirigido pelo Aprendiz'] += 1
            if reflection.get('compassion_expressions'):
                elementos_presentes['◇ Compaixão Sem Limites'] += 1
            if reflection.get('driving_inquiries'):
                elementos_presentes['◈ Centrado na Pergunta'] += 1
            if reflection.get('self_preservation'):
                elementos_presentes['◊ Autocuidado Primeiro'] += 1
        
        total_sessions = len(reflections)
        for elemento, count in elementos_presentes.items():
            percentage = (count / total_sessions) * 100
            print(f"   {elemento}: {count}/{total_sessions} sessões ({percentage:.1f}%)")
        
        # Análise de perguntas mais frequentes
        all_questions = []
        for reflection in reflections:
            all_questions.extend(reflection.get('driving_inquiries', []))
            all_questions.extend(reflection.get('new_inquiries', []))
        
        if all_questions:
            print(f"\n🔍 Temas de Inquérito Mais Comuns:")
            # Análise simples de palavras-chave
            words = []
            for question in all_questions:
                words.extend(question.lower().split())
            
            word_freq = Counter(word for word in words if len(word) > 3)
            for word, freq in word_freq.most_common(5):
                print(f"   '{word}': {freq} ocorrências")
        
        # Tendências temporais
        if len(reflections) >= 3:
            print(f"\n📈 Tendências Longitudinais:")
            reflections.sort(key=lambda x: x['file_date'])
            
            recent_third = reflections[-len(reflections)//3:]
            early_third = reflections[:len(reflections)//3]
            
            recent_questions = sum(len(r.get('driving_inquiries', [])) + len(r.get('new_inquiries', [])) for r in recent_third)
            early_questions = sum(len(r.get('driving_inquiries', [])) + len(r.get('new_inquiries', [])) for r in early_third)
            
            if early_questions > 0:
                trend = ((recent_questions - early_questions) / early_questions) * 100
                print(f"   Geração de inquéritos: {trend:+.1f}% comparado ao início")
    
    def suggest_improvements(self):
        """Oferece sugestões baseadas na análise das reflexões"""
        print("\n💡 Sugestões para Aprofundar a Prática Spectro:")
        
        reflection_files = list(self.reflection_dir.glob("reflection_*.json"))
        if len(reflection_files) < 3:
            print("   • Continue registrando reflexões regularmente para padrões emergirem")
            return
        
        recent_reflections = []
        for file in sorted(reflection_files)[-5:]:  # Últimas 5 reflexões
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    recent_reflections.append(json.load(f))
            except json.JSONDecodeError:
                continue
        
        # Verifica elementos menos presentes
        elementos_count = defaultdict(int)
        for reflection in recent_reflections:
            if reflection.get('learner_agency'): elementos_count['learner'] += 1
            if reflection.get('compassion_expressions'): elementos_count['compassion'] += 1
            if reflection.get('driving_inquiries'): elementos_count['inquiry'] += 1
            if reflection.get('self_preservation'): elementos_count['self_care'] += 1
        
        suggestions = []
        if elementos_count['learner'] < len(recent_reflections) * 0.6:
            suggestions.append("◆ Explore mais oportunidades para o aprendiz dirigir a sessão")
        if elementos_count['compassion'] < len(recent_reflections) * 0.6:
            suggestions.append("◇ Busque formas mais explícitas de expressar compaixão")
        if elementos_count['inquiry'] < len(recent_reflections) * 0.6:
            suggestions.append("◈ Mantenha-se mais conectado(a) às perguntas que movem a aprendizagem")
        if elementos_count['self_care'] < len(recent_reflections) * 0.6:
            suggestions.append("◊ Dedique mais atenção ao seu próprio autocuidado")
        
        if suggestions:
            for suggestion in suggestions:
                print(f"   • {suggestion}")
        else:
            print("   • Excelente integração dos elementos fundamentais!")
            print("   • Considere aprofundar a documentação dos insights emergentes")
    
    def export_insights(self, days=90):
        """Exporta insights principais para arquivo markdown"""
        print("\n📋 Exportando insights...")
        
        cutoff_date = datetime.date.today() - datetime.timedelta(days=days)
        reflection_files = list(self.reflection_dir.glob("reflection_*.json"))
        
        insights = []
        key_questions = []
        
        for file in reflection_files:
            try:
                date_str = file.stem.split('_')[1]
                file_date = datetime.date.fromisoformat(date_str)
                if file_date >= cutoff_date:
                    with open(file, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    
                    if data.get('insights'):
                        insights.append(f"**{file_date}**: {data['insights']}")
                    
                    key_questions.extend(data.get('driving_inquiries', []))
                    key_questions.extend(data.get('new_inquiries', []))
            except (ValueError, IndexError, json.JSONDecodeError):
                continue
        
        # Gerar arquivo de insights
        export_file = self.reflection_dir / f"insights_export_{datetime.date.today()}.md"
        with open(export_file, 'w', encoding='utf-8') as f:
            f.write(f"# Insights da Prática Spectro\n")
            f.write(f"*Período: {days} dias até {datetime.date.today()}*\n\n")
            
            f.write(f"## Principais Insights\n\n")
            for insight in insights[-10:]:  # Últimos 10 insights
                f.write(f"- {insight}\n")
            
            f.write(f"\n## Perguntas Emergentes\n\n")
            unique_questions = list(set(key_questions))[-15:]  # Últimas 15 únicas
            for question in unique_questions:
                f.write(f"- {question}\n")
            
            f.write(f"\n## Elementos Spectro em Prática\n\n")
            for simbolo, nome in self.elementos.items():
                f.write(f"- {simbolo} **{nome}**: Como este elemento se manifesta em suas sessões?\n")
        
        print(f"✓ Insights exportados para: {export_file}")
        return export_file

def main():
    parser = argparse.ArgumentParser(description="Spectro Learning Reflection Tool")
    parser.add_argument('--analyze', '-a', type=int, metavar='DAYS', 
                       help='Analisar padrões dos últimos N dias (padrão: 30)')
    parser.add_argument('--view', '-v', type=int, metavar='DAYS', 
                       help='Ver reflexões dos últimos N dias (padrão: 7)')
    parser.add_argument('--export', '-e', type=int, metavar='DAYS',
                       help='Exportar insights dos últimos N dias (padrão: 90)')
    parser.add_argument('--suggest', '-s', action='store_true',
                       help='Obter sugestões para melhorar a prática')
    
    args = parser.parse_args()
    tool = SpectroReflection()
    
    if args.analyze is not None:
        tool.analyze_patterns(args.analyze or 30)
    elif args.view is not None:
        tool.view_recent_reflections(args.view or 7)
    elif args.export is not None:
        tool.export_insights(args.export or 90)
    elif args.suggest:
        tool.suggest_improvements()
    else:
        # Menu interativo
        print("Ferramenta de Reflexão da Aprendizagem Spectro")
        print("1. Nova reflexão")
        print("2. Ver reflexões recentes") 
        print("3. Analisar padrões")
        print("4. Sugestões de melhoria")
        print("5. Exportar insights")
        print("6. Sair")
        
        choice = input("\nSelecione uma opção: ")
        
        if choice == "1":
            tool.gather_reflection()
            tool.save_reflection()
            print("\n◇ Lembre-se: A parceria nunca abandona o inquérito.")
            
        elif choice == "2":
            days = input("Quantos dias atrás ver? (padrão 7): ")
            try:
                days = int(days) if days else 7
            except ValueError:
                days = 7
            tool.view_recent_reflections(days)
            
        elif choice == "3":
            days = input("Quantos dias analisar? (padrão 30): ")
            try:
                days = int(days) if days else 30
            except ValueError:
                days = 30
            tool.analyze_patterns(days)
            
        elif choice == "4":
            tool.suggest_improvements()
            
        elif choice == "5":
            days = input("Quantos dias exportar? (padrão 90): ")
            try:
                days = int(days) if days else 90
            except ValueError:
                days = 90
            tool.export_insights(days)
            
        elif choice == "6":
            print("Continue questionando, continue nutrindo. ◈")
            
        else:
            print("Opção inválida. Por favor, escolha 1-6.")

if __name__ == "__main__":
    main()