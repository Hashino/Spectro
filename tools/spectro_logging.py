#!/usr/bin/env python3
"""
Sistema de Logs para Ferramentas Spectro

Implementa logging robusto e persistência de dados para as ferramentas
do projeto Spectro, seguindo princípios de transparência e reflexão.
"""

import logging
import json
import os
import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
import threading

class SpectroLogger:
    """Logger especializado para ferramentas Spectro com contexto filosófico"""
    
    def __init__(self, tool_name: str, log_level: str = "INFO"):
        self.tool_name = tool_name
        self.log_dir = Path.home() / ".spectro_logs"
        self.log_dir.mkdir(exist_ok=True)
        
        # Setup logging
        self.logger = logging.getLogger(f"spectro.{tool_name}")
        self.logger.setLevel(getattr(logging, log_level.upper()))
        
        # File handler
        log_file = self.log_dir / f"{tool_name}_{datetime.date.today()}.log"
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Console handler  
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Formatters
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        console_formatter = logging.Formatter(
            '%(levelname)s: %(message)s'
        )
        
        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        # Contexto Spectro
        self.session_context = {}
        self.inquiry_log = []
        
    def log_inquiry(self, question: str, context: str = ""):
        """Log especial para inquéritos - elemento central do Spectro"""
        self.inquiry_log.append({
            'timestamp': datetime.datetime.now().isoformat(),
            'question': question,
            'context': context
        })
        self.logger.info(f"◈ INQUIRY: {question}")
        
    def log_compassion(self, expression: str):
        """Log de expressões de compaixão"""
        self.logger.info(f"◇ COMPASSION: {expression}")
        
    def log_learner_agency(self, action: str):
        """Log de momentos de autonomia do aprendiz"""  
        self.logger.info(f"◆ LEARNER_AGENCY: {action}")
        
    def log_self_care(self, action: str):
        """Log de práticas de autocuidado"""
        self.logger.info(f"◊ SELF_CARE: {action}")
        
    def log_insight(self, insight: str, intensity: str = "medium"):
        """Log de insights emergentes"""
        self.logger.info(f"💡 INSIGHT[{intensity}]: {insight}")
        
    def log_error_with_compassion(self, error: Exception, context: str = ""):
        """Log de erros com abordagem compassiva"""
        self.logger.error(f"🌱 LEARNING_OPPORTUNITY: {str(error)} | Context: {context}")
        self.logger.debug(f"Technical details: {repr(error)}")
        
    def start_session(self, participants: List[str], topic: str):
        """Inicia sessão de logging contextual"""
        self.session_context = {
            'start_time': datetime.datetime.now().isoformat(),
            'participants': participants,
            'topic': topic,
            'session_id': self.generate_session_id()
        }
        self.logger.info(f"🚀 SESSION_START: {topic} with {', '.join(participants)}")
        
    def end_session(self, summary: str = ""):
        """Encerra sessão com resumo"""
        if self.session_context:
            duration = datetime.datetime.now() - datetime.datetime.fromisoformat(
                self.session_context['start_time']
            )
            self.logger.info(f"✅ SESSION_END: Duration {duration} | Summary: {summary}")
            
            # Salvar dados da sessão
            self.save_session_data(summary)
        
    def save_session_data(self, summary: str):
        """Salva dados completos da sessão"""
        if not self.session_context:
            return
            
        session_data = {
            **self.session_context,
            'end_time': datetime.datetime.now().isoformat(),
            'summary': summary,
            'inquiries': self.inquiry_log.copy(),
            'tool_name': self.tool_name
        }
        
        session_file = self.log_dir / f"session_{self.session_context['session_id']}.json"
        with open(session_file, 'w', encoding='utf-8') as f:
            json.dump(session_data, f, indent=2, ensure_ascii=False)
            
        self.logger.debug(f"Session data saved to {session_file}")
        
    def generate_session_id(self) -> str:
        """Gera ID único para sessão"""
        import hashlib
        timestamp = datetime.datetime.now().isoformat()
        return hashlib.md5(f"{self.tool_name}_{timestamp}".encode()).hexdigest()[:8]
        
    def get_recent_sessions(self, days: int = 7) -> List[Dict[str, Any]]:
        """Recupera sessões recentes para análise"""
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
        sessions = []
        
        for session_file in self.log_dir.glob("session_*.json"):
            try:
                with open(session_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                session_time = datetime.datetime.fromisoformat(data['start_time'])
                if session_time >= cutoff_date:
                    sessions.append(data)
                    
            except (json.JSONDecodeError, KeyError, ValueError):
                continue
                
        return sorted(sessions, key=lambda x: x['start_time'], reverse=True)
        
    def analyze_inquiry_patterns(self, days: int = 30) -> Dict[str, Any]:
        """Analisa padrões de inquérito nas sessões"""
        sessions = self.get_recent_sessions(days)
        all_inquiries = []
        
        for session in sessions:
            all_inquiries.extend(session.get('inquiries', []))
            
        if not all_inquiries:
            return {'total_inquiries': 0, 'patterns': []}
            
        # Análise simples de palavras-chave
        from collections import Counter
        words = []
        for inquiry in all_inquiries:
            words.extend(inquiry['question'].lower().split())
            
        common_themes = Counter(word for word in words if len(word) > 3).most_common(10)
        
        return {
            'total_inquiries': len(all_inquiries),
            'sessions_analyzed': len(sessions),
            'common_themes': common_themes,
            'avg_inquiries_per_session': len(all_inquiries) / len(sessions) if sessions else 0
        }

class SpectroDataPersistence:
    """Sistema de persistência de dados robusto para Spectro"""
    
    def __init__(self, data_dir: Optional[Path] = None):
        self.data_dir = data_dir or (Path.home() / ".spectro_data")
        self.data_dir.mkdir(exist_ok=True)
        self.backup_dir = self.data_dir / "backups"
        self.backup_dir.mkdir(exist_ok=True)
        self._lock = threading.Lock()
        
    def save_data(self, key: str, data: Any, create_backup: bool = True) -> bool:
        """Salva dados com backup automático"""
        try:
            with self._lock:
                file_path = self.data_dir / f"{key}.json"
                
                # Backup do arquivo existente
                if create_backup and file_path.exists():
                    backup_name = f"{key}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    backup_path = self.backup_dir / backup_name
                    import shutil
                    shutil.copy2(file_path, backup_path)
                
                # Salvar novos dados
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, indent=2, ensure_ascii=False, default=str)
                
                return True
                
        except Exception as e:
            logging.error(f"Error saving data for key {key}: {e}")
            return False
            
    def load_data(self, key: str, default: Any = None) -> Any:
        """Carrega dados com fallback para backup"""
        try:
            with self._lock:
                file_path = self.data_dir / f"{key}.json"
                
                if file_path.exists():
                    with open(file_path, 'r', encoding='utf-8') as f:
                        return json.load(f)
                        
                # Tentar backup mais recente
                backup_files = list(self.backup_dir.glob(f"{key}_*.json"))
                if backup_files:
                    latest_backup = max(backup_files, key=lambda x: x.stat().st_mtime)
                    with open(latest_backup, 'r', encoding='utf-8') as f:
                        logging.warning(f"Loaded from backup: {latest_backup}")
                        return json.load(f)
                        
                return default
                
        except Exception as e:
            logging.error(f"Error loading data for key {key}: {e}")
            return default
            
    def list_keys(self) -> List[str]:
        """Lista todas as chaves de dados disponíveis"""
        return [f.stem for f in self.data_dir.glob("*.json")]
        
    def cleanup_old_backups(self, days: int = 30):
        """Remove backups antigos"""
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=days)
        
        for backup_file in self.backup_dir.glob("*.json"):
            if datetime.datetime.fromtimestamp(backup_file.stat().st_mtime) < cutoff_date:
                backup_file.unlink()
                logging.info(f"Removed old backup: {backup_file}")

# Exemplo de uso integrado
def example_integrated_logging():
    """Exemplo de como usar o sistema de logging integrado"""
    
    # Setup
    logger = SpectroLogger("reflection_tool")
    persistence = SpectroDataPersistence()
    
    # Início de sessão
    logger.start_session(["Educador", "Aprendiz"], "Frações com receitas")
    
    # Durante a sessão
    logger.log_inquiry("Como dividir uma receita para mais pessoas?")
    logger.log_learner_agency("Aprendiz escolheu trabalhar com receita de bolo")
    logger.log_compassion("Paciência quando cálculos deram errado")
    logger.log_insight("Frações são proporções na vida real!")
    logger.log_self_care("Pausa para café quando senti cansaço")
    
    # Salvando dados
    session_data = {
        'reflections': ['insight1', 'insight2'],
        'timestamp': datetime.datetime.now().isoformat()
    }
    persistence.save_data("session_20260121", session_data)
    
    # Fim de sessão
    logger.end_session("Excelente integração dos elementos Spectro")
    
    # Análise
    patterns = logger.analyze_inquiry_patterns()
    print(f"Análise: {patterns}")

if __name__ == "__main__":
    example_integrated_logging()